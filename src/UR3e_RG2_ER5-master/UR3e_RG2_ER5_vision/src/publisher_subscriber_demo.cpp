#include <ros/ros.h>
#include "PublisherSubscriber.h"
#include <std_msgs/String.h>

template<>
void PublisherSubscriber<std_msgs::String, std_msgs::String>::subscriberCallback(const std_msgs::String::ConstPtr& recievedMsg)
{
	ROS_INFO(" I received the following: %s ", recievedMsg->data.c_str());
	ROS_INFO("Sending the received the message on 'echo', topic");
	std_msgs::String echo_msgs;
	echo_msgs.data = recievedMsg->data; 
	publisherObject.publish(echo_msgs);

}

int main(int argc, char **argv){
	ros::init(argc, argv, "publisher_subscriber_demo");
	PublisherSubscriber<std_msgs::String, std_msgs::String> parrot("echo", "chatter",1);
	ros::spin();
}