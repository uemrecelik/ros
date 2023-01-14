#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/odomexercises.py
import sys
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

##ROS nav_msgs/odometry Message 
##rosmsg show nav_msgs/Odometry
#The nav_msgs/Odometry  messsage stores an estimate of
# position and velocity of a robot in free space

 
nodeid = str(sys.argv[1])
nodename = "tb3_" + nodeid

def callback(msg):
 		print (msg.pose.pose)


def movetask():
	## stage pub = rospy.Publisher('robot_0/cmd_vel', Twist, queue_size=10)
	pub = rospy.Publisher(nodename +'/cmd_vel', Twist, queue_size=10)
	

	vel_msg = Twist()
	vel_msg.linear.x = 0.5
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0.2
	
	while not rospy.is_shutdown():
		#print(msg)
		pub.publish(vel_msg)
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	pub.publish(vel_msg)


rospy.init_node('movenode' , anonymous = True)
## stage odom_sub = rospy.Subscriber('robot_0/odom' , Odometry , callback=callback)
odom_sub = rospy.Subscriber(nodename +'/odom' , Odometry , callback=callback)
movetask()
rospy.spin()		