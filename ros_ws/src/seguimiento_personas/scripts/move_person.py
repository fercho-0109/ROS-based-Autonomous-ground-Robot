#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose, Twist
from math import atan2, sin, cos

def interpolate_points(p1, p2, t):
    x = p1[0] + (p2[0] - p1[0]) * t
    y = p1[1] + (p2[1] - p1[1]) * t
    return x, y

def calculate_orientation(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    yaw = atan2(dy, dx)
    return yaw

def move_person():
    rospy.init_node('move_person', anonymous=True)
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    rate = rospy.Rate(15)  # Frecuencia de publicación en Hz
    dt = 0.005  # Incremento de tiempo para la interpolación

    # Definir los puntos de la trayectoria
    trajectory = [(-9, -9), (-8, -9),(-6, -8), (-4, -8), (-1, -6), (1, -6),
                  (3, -4), (3, -2), (5, 1), (5, 4), (3, 6), (1, 6),
                  (-2, 5), (-5, 2), (-7, 2), (-9, 5), (-9, 7),
                  (-4, 9.5), (0, 9), (5, 8),
                  (7, 5), (7, 2), (5, -2), (1, -4), (-4, -4), (-7, -5), (-10, -7)]  
                  # Ejemplo de una trayectoria lineal en el eje x

    index = 0  # Índice para seguir la trayectoria
    t = 0.0  # Parámetro de interpolación

    while not rospy.is_shutdown():
        # Crea un objeto ModelState para representar el estado de la persona
        person_state = ModelState()
        person_state.model_name = 'person_walking'

        # Obtener los puntos de interpolación
        p1 = trajectory[index]
        p2 = trajectory[(index + 1) % len(trajectory)]

        # Interpolar la posición de la persona
        x, y = interpolate_points(p1, p2, t)

        # Establecer la nueva posición de la persona
        person_state.pose = Pose()
        person_state.pose.position.x = x
        person_state.pose.position.y = y
        person_state.pose.position.z = 0.0

        # Calcular la orientación de la persona
        yaw = calculate_orientation(p1, p2)
        # Ajustar la orientación de la cara
        desired_yaw = yaw + 1.5708  # 90 grados en radianes (ajustar según sea necesario)
        person_state.pose.orientation.z = sin(desired_yaw/ 2)
        person_state.pose.orientation.w = cos(desired_yaw/ 2)

        # Establecer la velocidad de la persona (opcional)
        person_state.twist = Twist()
        person_state.twist.linear.x =0 # (p2[0] - p1[0]) / dt  # Velocidad lineal en el eje x
        person_state.twist.angular.z = 0  # Velocidad angular en el eje z

        pub.publish(person_state)  # Publicar el nuevo estado de la persona

        # Actualizar el parámetro de interpolación
        t += dt

        # Verificar si se ha alcanzado el siguiente punto de la trayectoria
        if t >= 1.0:
            t = 0.0
            index = (index + 1) % len(trajectory)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_person()
    except rospy.ROSInterruptException:
        pass