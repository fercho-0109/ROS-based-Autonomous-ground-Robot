#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from std_msgs.msg import String


class PersonDetectionNode:
    def __init__(self):
        rospy.init_node('person_detection_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        self.detection_pub = rospy.Publisher('/image_with_detections', Image, queue_size=10)
        self.detection_pub_2 = rospy.Publisher('/detection_topic', Point, queue_size=10)
        self.person_detected_pub = rospy.Publisher('/detection_topic', String, queue_size=1)

        
        # self.cascade_path = '/home/alexis/ros_ws/src/seguimiento_personas/scripts/fullbody.xml'
        self.cascade_path = '/home/alexis/ros_ws/src/seguimiento_personas/scripts/haarcascade_lowerbody.xml'
        # self.cascade_path = rospy.get_param('~cascade_path', 'seguimiento_personas/haarcascade_lowerbody.xml')
        try:
            self.cascade = cv2.CascadeClassifier(self.cascade_path)
        except cv2.error as e:
            rospy.logerr('Error loading cascade: {}'.format(e))
        
        self.image_with_detections = None
        # self.cascade = cv2.CascadeClassifier(self.cascade_path)

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        detections = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
         # Ejemplo: Publicar las detecciones de personas en el tópico de salida

        for (x, y, w, h) in detections:
            cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(detections) > 0:
            rospy.loginfo('Person detected!')
            self.image_with_detections = cv_image
            self.publish_image_with_detections()

            # Obtener las coordenadas del rectángulo de la persona detectada
            x, y, w, h = detections[0]
            person_center_x = x + w / 2
            person_center_y = y + h / 2

            # Publicar la posición de la persona objetivo
            person_point = Point()
            person_point.x = person_center_x
            person_point.y = person_center_y
            person_point.z = 0.0  # No se utiliza en este ejemplo

            self.detection_pub_2.publish(person_point)
            # Publicar el mensaje 'person_detected' cuando se detecte una persona
            self.person_detected_pub.publish(String('person_detected'))


            
        if len(detections) == 0:
            rospy.loginfo('Person not detected!')

            
    def publish_image_with_detections(self):
        try:
            image_msg = self.bridge.cv2_to_imgmsg(self.image_with_detections, 'bgr8')
            self.detection_pub.publish(image_msg)
        except CvBridgeError as e:
            rospy.logerr(e)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        node = PersonDetectionNode()
        node.run()
    except rospy.ROSInterruptException:
        pass




