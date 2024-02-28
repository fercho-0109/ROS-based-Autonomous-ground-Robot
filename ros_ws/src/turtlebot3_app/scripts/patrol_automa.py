#! /usr/bin/env python3
# - *- coding: utf- 8 - *
import rospy
import actionlib
import tf
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from smach import State, StateMachine

class Waypoint(State):
    def __init__(self, w):
        State.__init__(self,outcomes=['success','stopped'])
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.client.wait_for_server()
        # Create Goal
        self.goal = MoveBaseGoal()
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.x = w[0]
        self.goal.target_pose.pose.position.y = w[1]
        q = tf.transformations.quaternion_from_euler(0,0,w[2])
        self.goal.target_pose.pose.orientation.x = q[0]
        self.goal.target_pose.pose.orientation.y = q[1]
        self.goal.target_pose.pose.orientation.z = q[2]
        self.goal.target_pose.pose.orientation.w = q[3]

    def execute(self, userdata):
        # Send Goal
        self.client.send_goal(self.goal)
        self.client.wait_for_result()
        if self.client.get_result() == None:
            return 'stopped'
        return 'success'


class PatrolAutoma():
    def __init__(self):
        rospy.init_node('patrol')

        # ------ PARAMETERS ------
        # waypoints:
        # [(x,y,ϑ),(x,y,ϑ),(x,y,ϑ)]
        self.waypoints = [(1.6,-0.6,0.7199),(1.5,1.5,2.7586),(-1.5,1.5,-2.0984),(-1.5,-1.5,-0.4026)]
        
        self.sm = StateMachine(outcomes=['terminated'])
        with self.sm:
            for i in range(len(self.waypoints)):
                # Add states: (name, Waypoint, transitions)
                StateMachine.add('W'+str(i),Waypoint(self.waypoints[i]),transitions={'success':'W'+str((i+1)%len(self.waypoints)), 'stopped':'terminated'})

    def loop(self):
        self.sm.execute()
        
        
if __name__ == '__main__':
    pa = PatrolAutoma()
    pa.loop()