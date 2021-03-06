#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include "UR3e_RG2_ER5_vision/SheeMsg.h"


typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}


// typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

// int main(int argc, char** argv)
// {
//   ros::init (argc, argv, "SheeMsgNode");
//   ros::NodeHandle nh;
//   ros::Publisher pub = nh.advertise<UR3e_RG2_ER5_vision::SheeMsg> ("SheeMsgTopic", 1);

//   UR3e_RG2_ER5_vision::SheeMsg msg;
//   msg.hey_name = "SheenMsg_Name";
//   msg.hey_age = 7;

//   ros::Rate loop_rate(4);
//   while (nh.ok())
//   {
//     // pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
//     pub.publish (msg);
//     ros::spinOnce ();
//     loop_rate.sleep ();
//   }
// }
