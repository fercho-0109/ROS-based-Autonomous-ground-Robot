#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelStates

def position_callback(data):
    # Obtener el índice de la persona en el arreglo de ModelStates
    index = data.name.index('person_walking')

    # Obtener la posición de la persona
    position = data.pose[index].position

    # Imprimir la posición en la consola
    rospy.loginfo("Posición de person_walking: x={}, y={}, z={}".format(position.x, position.y, position.z))

def subscribe_to_position():
    rospy.init_node('position_subscriber', anonymous=True)

    # Suscribirse al tópico '/gazebo/model_states' para obtener los estados de los modelos en Gazebo
    rospy.Subscriber('/gazebo/model_states', ModelStates, position_callback)

    # Mantener el nodo en ejecución
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_to_position()
    except rospy.ROSInterruptException:
        pass
