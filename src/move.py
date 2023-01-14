#!/usr/bin/env python3

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/move.py

import rospy

from geometry_msgs.msg import Twist

def moveRobot():

	rospy.init_node('move',anonymous = True)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	

	vel_msg = Twist()
	vel_msg.linear.x = 0.8
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 1
	
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
		
