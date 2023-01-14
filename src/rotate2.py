#!/usr/bin/env python3

#Umut Emre ÇELİK 18070006039

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/rotate2.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist


nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId

rospy.init_node(nodeName , anonymous = True)
pub = rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)

vel_msg = Twist()

vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

ctrl_c = False

def rotaterobot(speed, angle, clockwise, lspeed=0.0):
	
	rospy.loginfo("Let's rotate")
	angularspeed = speed * (math.pi/180)
	relativeangle = angle * (math.pi/180)
	rate = rospy.Rate(10)

	vel_msg.linear.x = lspeed
	vel_msg.angular.z = clockwise * abs(angularspeed)


	while not ctrl_c:
		connections = pub.get_num_connections()
		if connections > 0:
			pub.publish(vel_msg)
			break
		else:
			rate.sleep()

	t0 = rospy.Time.now().secs
	current_angle = 0


	while(current_angle < relativeangle):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().secs
		current_angle = angularspeed * (t1-t0)
		rate.sleep()

	stop_robot()

def shutdowntask():
	stop_robot()
	ctrl_c = True

def stop_robot():
	rospy.loginfo("shutdown time ! stop the robot")
	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

if __name__ == "__main__":
	try:
		rospy.on_shutdown(shutdowntask)
		rotaterobot(60.0 , 90.0 , -1 , 0)
	except rospy.ROSInterrupException:
		pass


