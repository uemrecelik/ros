// Umut Emre Celik 18070006039

#include <ros/ros.h>
#include <std_srvs/Empty.h>
#include <turtlesim/Spawn.h>

int main(int argc, char** argv)
{
	ros::init(argc,argv,"setcolor");
	ros::NodeHandle n;
	int color_r, color_g ,color_b;
	n.getParam("r" , color_r);
	n.getParam("g" , color_g);
	n.getParam("b" , color_b);

	ros::service::waitForService("clear");
	ros::param::set("background_r", color_r);
	ros::param::set("background_g", color_g);
	ros::param::set("background_b", color_b);

	ros::ServiceClient clearclient = n.serviceClient<std_srvs::Empty>("clear");
	std_srvs::Empty srv;

	clearclient.call(srv);

	return 0;
}