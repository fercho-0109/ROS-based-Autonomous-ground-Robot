#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class DetectionAndTracking:
    def __init__(self):
        rospy.init_node('detection_and_tracking', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


        self.no_person_counter = 0
        self.max_no_person_count = 5  # Número máximo de iteraciones sin detección de personas antes de detener el robot


        #self.cascade_path = '/home/alexis/ros_ws/src/seguimiento_personas/scripts/fullbody.xml'
        self.cascade_path = '/home/alexis/ros_ws/src/seguimiento_personas/scripts/haarcascade_lowerbody.xml'
        # self.cascade_path = rospy.get_param('~cascade_path', 'seguimiento_personas/haarcascade_lowerbody.xml')
        try:
            self.cascade = cv2.CascadeClassifier(self.cascade_path)
        except cv2.error as e:
            rospy.logerr('Error loading cascade: {}'.format(e))
            

        self.target_person = None
        self.cv_image= None
        self.prev_center_x = None
        self.prev_center_y = None

    def image_callback(self, msg):  
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        detections = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(detections) > 0:
            # Reiniciar el contador si se detecta una persona
            self.no_person_counter = 0
            # Si la persona objetivo no está establecida, seleccionamos la primera persona detectada
            if self.target_person is None:
                self.target_person = detections[0]
            else:
                 # Buscar la persona más cercana en cada iteración
                min_distance = float('inf')
                closest_person = None

                for detection in detections:
                    x, y, w, h = detection
                    center_x = x + w // 2
                    center_y = y + h // 2
                    distance = abs(center_x - self.cv_image.shape[1] // 2) + abs(center_y - self.cv_image.shape[0] // 2)

                    if distance < min_distance:
                        min_distance = distance
                        closest_person = detection

                # Actualizar la persona objetivo con la más cercana
                self.target_person = closest_person               

            # Realizar el seguimiento de la persona objetivo
            self.track_person()
        else:
            # Incrementar el contador si no se detecta ninguna persona
            self.no_person_counter += 1

            # Detener el robot si se supera el número máximo de iteraciones sin detección de personas
            if self.no_person_counter >= self.max_no_person_count:
                self.stop_robot()
                
    def stop_robot(self):
        # Detener el robot publicando un mensaje de velocidad lineal y angular cero
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        self.cmd_vel_pub.publish(twist_msg)

    def track_person(self):
        # Extraer las coordenadas de la persona objetivo
        x, y, w, h = self.target_person

        # Calcular el centro de la persona objetivo
        target_center_x = x + w // 2
        target_center_y = y + h // 2

        # Calcular los errores en el seguimiento
        error_x = target_center_x - self.cv_image.shape[1] // 2
        rospy.loginfo(f'error x {error_x}')
        error_y = target_center_y - self.cv_image.shape[0] // 2    
        
        # Realizar el control para el seguimiento
        twist_msg = Twist()
        twist_msg.linear.x = 0.175 + (-0.001 *error_y) # Velocidad lineal constante
        twist_msg.angular.z = -0.001 * error_x  # Control proporcional de la velocidad angular
        rospy.loginfo(f'ang vel {twist_msg.angular.z}')

        # Publicar el comando de velocidad
        self.cmd_vel_pub.publish(twist_msg)
       

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        node = DetectionAndTracking()
        node.run()
    except rospy.ROSInterruptException:
        pass