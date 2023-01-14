#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/projecttask1.py

import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId

rospy.init_node(nodeName , anonymous = True)
pub = rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)

vel_msg = Twist()
vel_msg.linear.x = 0.0
vel_msg.angular.z = 0


obstacle = False
direction = -1

def moveUntilObstacle():
	print(obstacle)

	while obstacle == False:
		vel_msg.linear.x = 10
		vel_msg.angular.z = 0
		pub.publish(vel_msg)

	#vel_msg.linear.x = 0	
	#pub.publish(vel_msg)

def rotateRobot(dir):
	vel_msg.linear.x = 0
	speed = 10.0
	angle = 90.0
	angularspeed=speed*(math.pi/180.0)
	relativeangle=angle*(math.pi/180.0)
	vel_msg.angular.z = angularspeed * dir
	t0 = rospy.Time.now().to_sec()
	current_angle = 0 
	speed = vel_msg.linear.x 
	while current_angle < relativeangle:
		pub.publish(vel_msg) 
		t1 = rospy.Time.now().to_sec()
		current_angle = angularspeed *(t1-t0) 	
	vel_msg.linear.x = 0
	vel_msg.angular.z =0
	pub.publish(vel_msg)



def moveDistance(distance):
	
	vel_msg.linear.x = 1
	rate = rospy.Rate(10)
	t0 = rospy.Time.now().to_sec() 
	current_distance = 0 
	speed = vel_msg.linear.x 
	
	while current_distance < distance:
		pub.publish(vel_msg) 
		t1 = rospy.Time.now().to_sec()
		current_distance = speed*(t1-t0) 
		rate.sleep()
	vel_msg.linear.x = 0





def callback(msg):
	global direction
	global obstacle
	obstacle = False
	for i in range(len(msg.ranges)):
		if i >= 110 and i <= 135 :
				if msg.ranges[i] < 0.5:
					obstacle = True
					for i in range(len(msg.ranges)):
						if i >= 220 and i <= 245 :
							print(msg.ranges[i])
							if msg.ranges[i] < 4.8:
								direction = -1
							else:
								direction = 1


							
def main():
	moveUntilObstacle()
	rotateRobot(direction)
	moveDistance(1.2)
	rotateRobot(direction)
	moveUntilObstacle()
	rotateRobot(direction)
	moveDistance(1.2)
	rotateRobot(direction)
	moveUntilObstacle()
	rotateRobot(direction)
	moveDistance(1.2)
	rotateRobot(direction)
	moveDistance(8)


									
	



sub = rospy.Subscriber(nodeName+'/base_scan', LaserScan , callback)# scan => for Gazebo
main()
rospy.spin()
