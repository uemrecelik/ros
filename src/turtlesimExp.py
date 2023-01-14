#!/usr/bin/env python3

#Umut Emre Celik 18070006039

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/midterm.py

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



def RightrotateRobot(speed,angle ,lspeed):
	clockwise = -1
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




def LeftrotateRobot(speed,angle ,lspeed):
	clockwise = 1
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




def moveRobot(distance):
	rospy.init_node('move')
	pub = rospy.Publisher(nodename +'/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	vel_msg.linear.x = 1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	rate = rospy.Rate(10)
	rospy.loginfo("Moving..")
	
	#distance = 2.0 #wish to travel 
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
		moveRobot(2) # first move (right)
		RightrotateRobot(10,88.5,0) # turn right
		moveRobot(0.25) # move down
		RightrotateRobot(10,88.1,0)#turn right second turn
		moveRobot(1.75)# move left
		LeftrotateRobot(10,88.5,0) #turn left
		moveRobot(0.25) # move down 2
		LeftrotateRobot(10,88.69,0) # turn left thirt turn
		moveRobot(4) #move right x2
		RightrotateRobot(10,88.9,0)# turn right to down
		moveRobot(0.25) # move down
		RightrotateRobot(10,88.25,0) # turn right 
		moveRobot(8) # move left double 
		LeftrotateRobot(10,89,0) # turn left
		moveRobot(0.3) # move down
		LeftrotateRobot(10,87.95,0) # turn left
		moveRobot(3.4) # move to start point


	except rospy.ROSInterruptException:
		pass
		
		
		
