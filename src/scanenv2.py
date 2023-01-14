#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/scanenv2.py

import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId

vel_msg = Twist()
vel_msg.linear.x = 0.5
vel_msg.angular.z = 0.0
minfrontdist = 0.9
stopdist = 0.7
stop = 0
obstacle = False
speed = 0.5
sspeed = 0.1
minleft = 1000000.0
minright = 1000000.0
maxleft = -1
maxright = -1

rospy.init_node(nodeName , anonymous = True)
pub = rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)

def rotateRobot(dir):
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0.3 * dir
	pub.publish(vel_msg)

def obstaclefunc(minleft,minright):
	if stop == 1:
		speed = sspeed
	if minleft < minright:
		rotateRobot(+1)
	elif minleft >= minright:
		rotateRobot(-1)


def callback(msg):
	obstacle = False
	size = len(msg.ranges)
	global minleft
	global minright
	global maxleft
	global maxright

	for i in range(0,size):
		if float(msg.ranges[i]<minfrontdist):
			obstacle = True
		if float(msg.ranges[i]<stopdist):
			stop = 1
		if i < size/2:
			minleft = min(minleft, float(msg.ranges[i]))	
			maxleft = max(maxleft,float(msg.ranges[i]))
		else:
			minright = min(minright, float(msg.ranges[i]))
			maxright = max(maxright,float(msg.ranges[i]))
		if obstacle:
			obstaclefunc(minleft,minright)
		else:
			vel_msg.linear.x = speed
			vel_msg.angular.z = 0.0
			pub.publish(vel_msg)

sub = rospy.Subscriber(nodeName+'/base_scan', LaserScan , callback)# scan => for Gazebo
rospy.spin()						




