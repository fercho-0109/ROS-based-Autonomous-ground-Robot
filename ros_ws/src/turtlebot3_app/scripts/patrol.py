#! /usr/bin/env python3
# - *- coding: utf- 8 - *
import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class Patrol():
    def __init__(self):
        rospy.init_node('patrol')
        # ------ PARAMETERS ------
        # list of waypoint:
        # [(x1,y1,ϑ1),(x2,y2,ϑ2),(x3,y3,ϑ3)]
        self.waypoints = [( 1.6,-0.6, 0.7199),\
                          ( 1.5, 1.5, 2.7586),\
                          (-1.5, 1.5,-2.0984),\
                          (-1.5,-1.5,-0.4026)]
        # ------ ACTIONS ------
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def loop(self):
        while not rospy.is_shutdown():
            for w in self.waypoints:
                # Create Goal
                goal = MoveBaseGoal()
                goal.target_pose.header.frame_id = 'map'
                goal.target_pose.pose.position.x = w[0]
                goal.target_pose.pose.position.y = w[1]
                q = tf.transformations.quaternion_from_euler(0,0,w[2])
                goal.target_pose.pose.orientation.x = q[0]
                goal.target_pose.pose.orientation.y = q[1]
                goal.target_pose.pose.orientation.z = q[2]
                goal.target_pose.pose.orientation.w = q[3]
                # Send Goal
                self.client.send_goal(goal)
                print('Raeaching the pose: '+str(w))
                self.client.wait_for_result()
                print('Pose reached')

if __name__ == '__main__':
    p = Patrol()
    p.loop()