#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
#include <tf/tf.h>
#include <geometry_msgs/Pose2D.h>
#include <math.h>

ros::Publisher pub;
geometry_msgs::Twist msg;
geometry_msgs::Pose2D current_pose;

void callback(const nav_msgs::Odometry::ConstPtr &msg)
{
	//ROS_INFO("%s", msg->header.frame_id.c_str());
	//ROS_INFO("%f", msg->twist.twist.linear.x);
	//ROS_INFO("%f", msg->pose.pose.position.x);

	current_pose.x = msg->pose.pose.position.x;
	current_pose.y = msg->pose.pose.position.y;

	//ROS uses quaternions (4 dimensional number system) to track and apply rotations. 
	//A quaternion has 4 components (x,y,z,w).
	//Good way for describing 3D orientation. 
	//Also, Euler angles for rotation.
	tf::Quaternion q(
		msg->pose.pose.orientation.x,
		msg->pose.pose.orientation.y,
		msg->pose.pose.orientation.z,
		msg->pose.pose.orientation.w);

	//...
}

void move(ros::NodeHandle n)
{
	pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
	ros::Rate loop_rate(10);

	//...
}

void rotate1(ros::NodeHandle n)
{
	pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
	ros::Rate loop_rate(10);

	//...
}

void rotate2(ros::NodeHandle n)
{
	pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
	ros::Rate loop_rate(10);

	//...
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "odomnode");
	ros::NodeHandle n;

	ros::Subscriber sub = n.subscribe("/odom", 1000, callback);

	//...


	ros::spin();

	return 0;
}



