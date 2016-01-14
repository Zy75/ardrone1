
ROS: indigo

PC : ubuntu 14.04

kinect: kinect xbox 360 ( not v2)

uses ardrone_autonomy ROS package

problems:

1. a little weak to disturbances.

2. Average depth is unstable. That is, when drone is horizontally seen, only the nearest is detected. But when the drone has tilt, far point is also detected. 

3. 

-----------------------------------procedure---------------------------------------------

terminal1: roscore

terminal2: roslaunch freenect_launch freenect.launch

terminal3: cd ~/catkin_ws 

          source devel/setup.bash

          roslaunch ardrone1 driver_with_params.launch
   
terminal4: cd ~/catkin_ws

           source devel/setup.bash

           rosrun ardrone1 ardrone1.py

terminal5: takeoff.sh ( rostopic pub -1 /ardrone/takeoff std_msgs/Empty )

terminal6: land.sh ( rostopic pub -1 /ardrone/land std_msgs/Empty )  

