#!/usr/bin/env python3

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/movedistance.py

import rospy
import sys
from geometry_msgs.msg import Twist

#nodeid = str(sys.argv[1])
#nodename = "turtle" + nodeid

def moveRobot():
	rospy.init_node('move')
	pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	rate = rospy.Rate(10)
	rospy.loginfo("Moving..")
	
	distance = 2.0 #wish to travel 
	t0 = rospy.Time.now().to_sec() # current time
	current_distance = 0 # will be uptadeted in loop
	speed = vel_msg.linear.x #speed of move 
	
	while current_distance < distance:
		pub.publish(vel_msg) #publish velocity message
		t1 = rospy.Time.now().to_sec() # get current time
		current_distance = speed*(t1-t0) 
		rate.sleep()
	
	vel_msg.linear.x = 0 # stop movment	
	vel_msg.angular.z = 0
	
	
if __name__ == "__main__":
	try:
		moveRobot()
	except rospy.ROSInterrupException:
		pass
		
		
		
