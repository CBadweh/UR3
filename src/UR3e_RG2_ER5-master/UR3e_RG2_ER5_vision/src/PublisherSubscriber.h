// Create node that sub and pub 
#ifndef PUBLISHER_SUBSCRIBER_H
#define PUBLISHER_SUBSCRIBER_H

#include <ros/ros.h>
#include <string>


template<typename PublishT, typename SubscribeT>
class PublisherSubscriber
{
public:
	PublisherSubscriber() {}
	PublisherSubscriber(std::string publisheTopicName, std::string subscribeTopicName, int queueSize)
	{
		publisherObject = nH.advertise<PublishT>(publisheTopicName,queueSize);
		subscriberObject = nH.subscribe<SubscribeT>(subscribeTopicName, queueSize, &PublisherSubscriber::subscriberCallback, this);
	}
	void subscriberCallback( const typename SubscribeT::ConstPtr& recieveMsg);

protected:
	ros::Subscriber subscriberObject;
	ros::Publisher publisherObject;
	ros::NodeHandle nH; 
};

#endif