#!/usr/bin/env python3
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/projecttask2.py

import sys
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt
from tf.transformations import euler_from_quaternion
from finalsrv.srv import finalsrv,finalsrvResponse



nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId

if nodeName =="robot_0":
    goal_param_x = rospy.get_param("goalX_r1")
    goal_param_y = rospy.get_param("goalY_r1")
if nodeName == "robot_1":
    goal_param_x = rospy.get_param("goalX_r2")
    goal_param_y = rospy.get_param("goalY_r2")



class MoveToGoal():

    def __init__(self):
    
        rospy.init_node('move', anonymous=True)    
        self.pub = rospy.Publisher(nodeName +'/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber(nodeName +'/odom', Odometry, self.callback) # Pose To Odom

        self.roll = 0
        self.pitch = 0 
        self.yaw = 0

        
        self.goalx = goal_param_x
        self.goaly = goal_param_y
       
      


        self.positionx = 0
        self.positiony = 0 
        self.position = Odometry()  


        self.rate = rospy.Rate(10)

    def callback(self, msg):
        
        self.positionx = msg.pose.pose.position.x
        self.positiony = msg.pose.pose.position.y


        self.orientation_q = msg.pose.pose.orientation



                
 
        self.orientation_list = [self.orientation_q.x, self.orientation_q.y, self.orientation_q.z, self.orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (self.orientation_list)
        #print(self.positionx, self.positiony, self.yaw)
        

    def euclidean_distance(self): 
        ##return sqrt(pow((self.goalx - self.positionx), 2) + pow((self.goaly - self.positiony), 2))
        rospy.wait_for_service("eucServer")
        try:
            eucDist= rospy.ServiceProxy("eucServer",finalsrv)
            response = eucDist(self.goaly, self.positiony, self.goalx, self.positionx)
           # rospy.loginfo(response.res)
            return response.res
        except Exception as e:
            print(e)    
   


    def linear_vel(self):
        return 1.5 * self.euclidean_distance()

    def steering_angle(self):
        return atan2(self.goaly - self.positiony, self.goalx - self.positionx)

    def angular_vel(self):
        return 6 * (self.steering_angle() - self.yaw) 

    def move2goal(self):

        
        vel_msg = Twist()
        while self.euclidean_distance() >= 0.01:


            vel_msg.linear.x = self.linear_vel()
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel()
            self.pub.publish(vel_msg)
            self.rate.sleep()


        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.pub.publish(vel_msg)


        rospy.spin()

if __name__ == '__main__':





    try:
        x = MoveToGoal()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass