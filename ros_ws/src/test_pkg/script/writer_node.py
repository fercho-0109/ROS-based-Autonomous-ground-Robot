#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from random import random

rospy.init_node('writer')
pub = rospy.Publisher('data_topic', Int32)
rate = rospy.Rate(1)
count = 0
while not rospy.is_shutdown():
    data=int(100*random())
    pub.publish(data)
    rate.sleep()