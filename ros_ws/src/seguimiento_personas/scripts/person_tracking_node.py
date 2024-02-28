#! /usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

class PersonTrackingNode:
    def __init__(self):
        rospy.init_node('person_tracking_node', anonymous=True)
        self.target_sub = rospy.Subscriber('/detection_topic', Point, self.target_callback)
        self.cmd_vel_pub  = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.target_x = 0.0  # Posición x del objetivo
        self.target_y = 0.0  # Posición y del objetivo

    def target_callback(self, target):
        rospy.loginfo('Received target position: x={}, y={}'.format(target.x, target.y))
        self.target_x = target.x
        self.target_y = target.y

    def calculate_velocity(self, current_x):
        # Parámetros del control proporcional
        kp = 0.5  # Ganancia proporcional

        # Error de seguimiento
        error = self.target_x - current_x

        # Cálculo de la velocidad de movimiento deseada
        velocity = kp * error

        # Limitar la velocidad a un rango máximo
        max_velocity = 0.5  # Velocidad máxima permitida
        if velocity > max_velocity:
            velocity = max_velocity
        elif velocity < -max_velocity:
            velocity = -max_velocity
       
 

        # Crear un objeto Twist para almacenar las velocidades
        vel_msg = Twist()
        vel_msg.linear.x = velocity
        #vel_msg.angular.z = angular_vel

        # Publicar las velocidades en el tópico "/cmd_vel"
        self.cmd_vel_pub.publish(vel_msg)
        return str(velocity)

    def run(self):
        rate = rospy.Rate(10)  # Frecuencia de publicación del mensaje de velocidad (10 Hz)

        while not rospy.is_shutdown():
            # Implementar aquí la lógica de control para el seguimiento de la persona

            # Ejemplo: Obtener la posición actual del robot (solo se utiliza la posición x)
            current_x = 0.0  # Obtener la posición actual en el eje x del robot (requiere la lógica de obtención de la posición actual del robot)

            # Calcular la velocidad deseada
            velocity = self.calculate_velocity(current_x)

            # Publicar la velocidad como mensaje de tipo String
             # self.velocity_pub.publish(velocity)

            rate.sleep()

if __name__ == '__main__':
    try:
        node = PersonTrackingNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
