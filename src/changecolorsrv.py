#!/usr/bin/env python3

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/changecolorsrv.py

import rospy
from std_srvs.srv import Empty
from turtlesim.srv import*


rospy.init_node('setcolor' , anonymous = True)


color_r = rospy.get_param("r")
color_g = rospy.get_param("g")
color_b = rospy.get_param("b")

print(color_r,color_g,color_b)

rospy.wait_for_service("clear")

print("clear working")

rospy.set_param("background_r" , color_r)
rospy.set_param("background_g" , color_g)
rospy.set_param("background_b" , color_b)

clear_background=rospy.ServiceProxy("clear", Empty)

clear_background()