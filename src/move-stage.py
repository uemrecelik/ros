#!/usr/bin/env python3

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/move-stage.py

import rospy
import sys

from geometry_msgs.msg import Twist

nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId


def moveRobot():

	##rospy.init_node('move')
	##pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	##pub = rospy.Publisher('robot_0/cmd_vel', Twist, queue_size=10)

	rospy.init_node(nodeName , anonymous = True)
	pub = rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)

	vel_msg = Twist()
	vel_msg.linear.x = 2
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		#print(msg)
		pub.publish(vel_msg)
		rate.sleep()



if __name__ == "__main__":
	try:
		moveRobot()
	except rospy.ROSInterrupException:
		pass
		
