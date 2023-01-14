#!/usr/bin/env python3

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/subscribeword.py

import rospy
from std_msgs.msg import String

rospy.init_node('stringsub')

def callbackfunc(msg):
	print(msg)


sub =rospy.Subscriber('/words', String, callbackfunc)
rospy.spin()

