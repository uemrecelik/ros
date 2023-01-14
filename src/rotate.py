#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/rotate.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist

nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid

rospy.init_node(nodename ,anonymous=True)

#rospy.init_node('move')
pub = rospy.Publisher(nodename+'/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0


def moveRobot(speed,angle ,lspeed,clockwise):
	angularspeed=speed*(math.pi/180.0)
	relativeangle=angle*(math.pi/180.0)
	vel_msg.linear.x = lspeed
	vel_msg.angular.z = angularspeed * clockwise
	
	
	rate = rospy.Rate(10)
	rospy.loginfo("Moving..")
	
	#distance = 2.0 #wish to travel 
	t0 = rospy.Time.now().to_sec() # current time
	current_angle = 0 # will be uptadeted in loop
	speed = vel_msg.linear.x #speed of move 
	
	while current_angle < relativeangle:
		pub.publish(vel_msg) #publish velocity message
		t1 = rospy.Time.now().to_sec() # get current time
		current_angle = angularspeed *(t1-t0) 
		
		rate.sleep()
	
	
	 #stop movment
	vel_msg.linear.x = 0 	
	vel_msg.angular.z = 0
	pub.publish(vel_msg)
	
	
if __name__ == "__main__":
	try:
		if nodeid == '1':
			moveRobot(5,60,0,-1)
		else:	
			moveRobot(10,90,0,1)
	except rospy.ROSInterrupException:
		pass
		
		
		
