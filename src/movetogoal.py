#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/movetogoal.py


import sys
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


nodeId = str(sys.argv[1])
nodeName = "turtle" + nodeId


if nodeId == '1':
    args = int(sys.argv[1])
if nodeId == '2':
    args = int(sys.argv[2])
    


class Turtlebot:


    

    def __init__(self , x):
        rospy.init_node('turtlenode', anonymous=True)
        self.pub=rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)
        self.sub=rospy.Subscriber(nodeName + '/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate=rospy.Rate(10)
        self.x = sys.argv[1]

    def update_pose(self, data):
        self.pose = data

    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x-self.pose.x),2.0)+pow((goal_pose.y-self.pose.y),2.0))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y-self.pose.y, goal_pose.x-self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose)-self.pose.theta)

    def move2goal(self):
        goalpose = Pose()
        goalpose.x = args
        goalpose.y = 2
        tolerance = 0.01
        vel_msg = Twist()
        while self.euclidean_distance(goalpose) >= tolerance:
            vel_msg.linear.x = self.linear_vel(goalpose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goalpose)
            self.pub.publish(vel_msg)
            self.rate.sleep()
        #Stop the robot
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.pub.publish(vel_msg)

if __name__ == "__main__":
    try:
        if nodeId == '1':
        
            x = Turtlebot(sys.argv[1])
            x.move2goal()
        else :
            x = Turtlebot(3)
            x.move2goal()

    except rospy.ROSInterruptException:
        pass
