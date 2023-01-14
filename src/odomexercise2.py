#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/odomexercise2.py

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry




def callback(msg):


    rospy.loginfo(msg.pose.pose)



def move():
    rate = rospy.Rate(10)
    pub = rospy.Publisher("robot_0/cmd_vel",Twist,queue_size=10) 
    vel_msg = Twist()
    vel_msg.linear.x  = 0
    vel_msg.linear.y  = 0
    vel_msg.linear.z  = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    
    while not rospy.is_shutdown():
        vel_msg.linear.x = 0.2
        pub.publish(vel_msg)
        rospy.spin()
        rate.sleep()





if __name__ == "__main__":
    rospy.init_node("odomnode",anonymous=True)
    odom_sub = rospy.Subscriber("robot_0/odom",Odometry,callback=callback)
    move()
    rospy.spin()