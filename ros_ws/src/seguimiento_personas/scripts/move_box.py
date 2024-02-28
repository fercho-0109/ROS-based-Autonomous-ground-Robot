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

def move_box():
    rospy.init_node('move_box', anonymous=True)
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    rate = rospy.Rate(50)  # Frecuencia de publicación en Hz
    dt = 0.01  # Incremento de tiempo para la interpolación

    # Definir los puntos de la trayectoria
    trajectory = [(1.0, 0.0), (4.0, 5.0), (7.0, 0.0)]  # Ejemplo de una trayectoria lineal en el eje x

    index = 0  # Índice para seguir la trayectoria
    t = 0.0  # Parámetro de interpolación

    while not rospy.is_shutdown():
        # Crea un objeto ModelState para representar el estado de la caja
        box_state = ModelState()
        box_state.model_name = 'unit_box'  # Reemplaza 'unit_box' con el nombre real de tu caja

        # Obtener los puntos de interpolación
        p1 = trajectory[index]
        p2 = trajectory[(index + 1) % len(trajectory)]

        # Interpolar la posición de la caja
        x, y = interpolate_points(p1, p2, t)

        # Establecer la nueva posición de la caja
        box_state.pose = Pose()
        box_state.pose.position.x = x
        box_state.pose.position.y = y
        box_state.pose.position.z = 0.0

        # Calcular la orientación de la caja
        yaw = calculate_orientation(p1, p2)
        box_state.pose.orientation.z = sin(yaw / 2)
        box_state.pose.orientation.w = cos(yaw / 2)

        # Establecer la velocidad de la caja (opcional)
        box_state.twist = Twist()
        box_state.twist.linear.x = 0.5#(p2[0] - p1[0]) / dt  # Velocidad lineal en el eje x
        box_state.twist.angular.z = 0  # Velocidad angular en el eje z

        pub.publish(box_state)  # Publicar el nuevo estado de la caja

        # Actualizar el parámetro de interpolación
        t += dt

        # Verificar si se ha alcanzado el siguiente punto de la trayectoria
        if t >= 1.0:
            t = 0.0
            index = (index + 1) % len(trajectory)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_box()
    except rospy.ROSInterruptException:
        pass
