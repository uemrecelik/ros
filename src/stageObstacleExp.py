#!/usr/bin/env python3

#Umut Emre Celik 18070006039

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/midterm2.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist

nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid


rospy.init_node('move')
pub = rospy.Publisher(nodename+'/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0



def rotateRobot(speed,angle ,lspeed,clockwise):
	angularspeed=speed*(math.pi/180.0)
	relativeangle=angle*(math.pi/180.0)
	vel_msg.linear.x = lspeed
	vel_msg.angular.z = angularspeed * clockwise
	
	
	rate = rospy.Rate(10)
	rospy.loginfo("Rotating..")
	
	#distance = 2.0 #wish to travel 
	t0 = rospy.Time.now().to_sec() # current time
	current_angle = 0 # will be uptadeted in loop
	speed = vel_msg.linear.x #speed of move 
	
	while current_angle < relativeangle:
		pub.publish(vel_msg) #publish velocity message
		t1 = rospy.Time.now().to_sec() # get current time
		current_angle = angularspeed *(t1-t0) 
		
		rate.sleep()




if __name__ == "__main__":
	try:
		rotateRobot(30,160.0,0.25,-1)
		rotateRobot(30,180.0,0.40,-1)
		rotateRobot(30,180.0,0.55,-1)
		rotateRobot(30,180.0,0.70,-1)
		rotateRobot(30,65.0,0.85,-1)
		
	except rospy.ROSInterruptException:
		pass