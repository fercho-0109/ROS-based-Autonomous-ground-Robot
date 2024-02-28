# ROS-based-Autonomous-ground-Robot

Code developed for "A. Marino, - Person Tracking System using Robot Turtlebot3 ".  
Master's student "Calabria University".  
For any questions or suggestions write to alexismarino0109@gmail.com

# Sumary.
The project encompasses the development of a person tracking system composed of two main nodes: the person move node and the person detection and tracking node.
The person detection node employs an OpenCV cascade classifier to detect people in the images captured by the TurtleBot3's camera. The detection information is published on a ROS topic, enabling other nodes in the system to access it.
The person move node is used to move a person to have a dynamic environment. The detection and tracking node utilizes visual tracking techniques to estimate the position of the detected person as they move within the robot's field of view. A proportional control algorithm is implemented to adjust the robot's angular velocity based on the tracking error, ensuring smooth and accurate tracking.
The steps followed during the development of the project are:
- Problem Identification
- Requirements identification
- Software and Hardware Setup
- Person_move Node
- Person detection_and_tracking Node
- Control Algorithm Implementation
- Integration and Testing


# Prerequisites
- The code was created and tested on ROS 1
- It is necesary instal Gazebo to simulate the enviroment

# File description
The repository contains the main file
1. **ros_ws**: this folder contains the workspace generated for this project

# Example to run the experiment  
**"ROS Simulation"**
1. run the ros master usin: roscore. 
2. Go to the environment: cd ros_ws.
3. Open the enviroment using :roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
4. Place a person un the environment and any obtacle deseried
5. Run the first node: rosrun seguimiento_personas move_person.py
6. Run the second node: rosrun seguimiento_personas detection_and_tracking.py
7. Gazebo should start to show the results  
![image](https://github.com/fercho-0109/ROS-based-Autonomous-ground-Robot/assets/40362695/975d58de-6ae1-494e-ad09-e10d8fee276a)










  


