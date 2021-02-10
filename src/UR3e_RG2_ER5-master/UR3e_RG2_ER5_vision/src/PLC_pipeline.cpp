
// source: https://stackoverflow.com/questions/61589904/not-correct-orientation-of-the-obb-box
//https://pcl.readthedocs.io/en/latest/moment_of_inertia.html#moment-of-inertia

#include <pcl/visualization/cloud_viewer.h>
#include <iostream>
#include <pcl/io/io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/features/integral_image_normal.h>
#include <pcl/features/normal_3d.h>
#include <ros/ros.h>
#include <tf/transform_datatypes.h>
#include <tf/transform_listener.h>
#include <tf/transform_broadcaster.h>
#include <sensor_msgs/PointCloud2.h> //hydro

// PCL specific includes
#include <pcl_conversions/pcl_conversions.h> //hydro
#include "pcl_ros/transforms.h"

#include <pcl/filters/voxel_grid.h>
#include <pcl/filters/passthrough.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/segmentation/extract_clusters.h>
#include <pcl/filters/crop_box.h>
#include <pcl/filters/statistical_outlier_removal.h>
#include <tf_conversions/tf_eigen.h>
#include <pcl/segmentation/extract_polygonal_prism_data.h>
#include <vector>
#include <thread>

#include <pcl/features/moment_of_inertia_estimation.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/visualization/cloud_viewer.h>
#include <visualization_msgs/MarkerArray.h>
#include <visualization_msgs/Marker.h>
#include <cmath>

// #include "UR3e_RG2_ER5_vision/Msg.h"
#include "UR3e_RG2_ER5_vision/UR3Msg.h"

ros::Publisher pub, pub2, markers_pub_;

void cloud_cb(const sensor_msgs::PointCloud2::ConstPtr &msg){

    // Convert to pcl point cloud
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_msg (new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::fromROSMsg(*msg,*cloud_msg);
    //ROS_DEBUG("%s: new ponitcloud (%i,%i)(%zu)",_name.c_str(),cloud_msg->width,cloud_msg->height,cloud_msg->size());
       
  //==========instantiate class and Calculation ==============
  // set input cloud and start the compuatioinal process
  pcl::MomentOfInertiaEstimation <pcl::PointXYZRGB> feature_extractor;
  feature_extractor.setInputCloud (cloud_msg);
  feature_extractor.compute ();

  // This is were we declare all necessary variables needed to store descriptors and bounding boxes.
  std::vector <float> moment_of_inertia;
  std::vector <float> eccentricity;
  pcl::PointXYZRGB min_point_AABB; // Code C added 
  pcl::PointXYZRGB max_point_AABB; // Code C added 
  pcl::PointXYZRGB min_point_OBB;
  pcl::PointXYZRGB max_point_OBB;
  pcl::PointXYZRGB position_OBB;
  Eigen::Matrix3f rotational_matrix_OBB;
  float major_value, middle_value, minor_value;
  Eigen::Vector3f major_vector, middle_vector, minor_vector;
  Eigen::Vector3f mass_center;

  // These lines show how to access computed descriptors and other features.
  feature_extractor.getMomentOfInertia (moment_of_inertia);
  feature_extractor.getEccentricity (eccentricity);
  feature_extractor.getAABB (min_point_AABB, max_point_AABB); // Added by C 
  feature_extractor.getOBB (min_point_OBB, max_point_OBB, position_OBB, rotational_matrix_OBB);
  feature_extractor.getEigenValues (major_value, middle_value, minor_value);
  feature_extractor.getEigenVectors (major_vector, middle_vector, minor_vector);
  feature_extractor.getMassCenter (mass_center);


  //========= For Visualizaiton ========================
  // OBB
  Eigen::Vector3f position (position_OBB.x, position_OBB.y, position_OBB.z);
  Eigen::Quaternionf quat (rotational_matrix_OBB);
  // cout << " orientation x  = " << quat.x() <<  endl;
  // cout << " orientation y = "  << quat.y() <<  endl;
  // cout << " orientation z = "  << quat.z() <<  endl;
  // cout << " orientation w = "  << quat.w() <<  endl;
  // cout << " postion x  = " << position_OBB.x <<  endl;
  // cout << " postion y  = " << position_OBB.y <<  endl;
  // cout << " postion z  = " << position_OBB.z <<  endl;

  // AABB
  cout << " min_point_AABB x  = " << min_point_AABB.x <<  endl;
  cout << " min_point_AABB y = "  << min_point_AABB.y <<  endl;
  cout << " min_point_AABB z = "  << min_point_AABB.z <<  endl;
  cout << " max_point_AABB x  = " << max_point_AABB.x <<  endl;
  cout << " max_point_AABB y  = " << max_point_AABB.y <<  endl;
  cout << " max_point_AABB z  = " << max_point_AABB.z <<  endl;



   

  //======= Covert PointCloud to ROS msg ===========
  //Publish points
  sensor_msgs::PointCloud2 cloud_publish;
  pcl::toROSMsg(*cloud_msg,cloud_publish);
  pub.publish(cloud_publish);

  //======== PUBLISHING OBJECT OF INTERESTED POSE AND RADIUS =========
  // init Ojb of interested's message type 
  UR3e_RG2_ER5_vision::UR3Msg UR3_msg;
  UR3_msg.Obj_name = "Detected_Obj";
  UR3_msg.Obj_Pose.position.x =  (max_point_AABB.x + min_point_AABB.x)/2;
  UR3_msg.Obj_Pose.position.y =  (max_point_AABB.y + min_point_AABB.y)/2;
  UR3_msg.Obj_Pose.position.z =  (max_point_AABB.z + min_point_AABB.z)/2;
  // Radius in y axis
  UR3_msg.Radius = (max_point_AABB.y - min_point_AABB.y)/2;
  pub2.publish(UR3_msg);
  //============Visualisation Marker=============
  //                  AABB

  //=====For single Point 
  std::string ns; 
  float r; 
  float g; 
  float b;
  visualization_msgs::MarkerArray msg_marker;
  visualization_msgs::Marker bbx_marker;
  bbx_marker.header.frame_id = "kinect_optical_link";
  bbx_marker.header.stamp = ros::Time::now();
  bbx_marker.ns = ns;
  bbx_marker.type = visualization_msgs::Marker::SPHERE;
  bbx_marker.action = visualization_msgs::Marker::ADD;
  bbx_marker.pose.position.x =  (max_point_AABB.x + min_point_AABB.x)/2;
  bbx_marker.pose.position.y =  (max_point_AABB.y + min_point_AABB.y)/2;
  bbx_marker.pose.position.z =  (max_point_AABB.z + min_point_AABB.z)/2;
  bbx_marker.pose.orientation.x = 0.0;
  bbx_marker.pose.orientation.y = 0.0;
  bbx_marker.pose.orientation.z = 0.0;
  bbx_marker.pose.orientation.w = 1.0;
  bbx_marker.scale.x = max_point_AABB.x - min_point_AABB.x;
  bbx_marker.scale.y = max_point_AABB.y - min_point_AABB.y;
  bbx_marker.scale.z = max_point_AABB.z - min_point_AABB.z;
  bbx_marker.color.b = b;
  bbx_marker.color.g = g;
  bbx_marker.color.r = r;
  bbx_marker.color.a = 0.4;
  bbx_marker.lifetime = ros::Duration();
  msg_marker.markers.push_back(bbx_marker);
  markers_pub_.publish(msg_marker);


}




int
main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "Analyzing_Obj");
  ros::NodeHandle nh;
  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe ("/extract_plane_indices/output", 200, cloud_cb);  //topic subscribe to
  // Create a ROS publisher for the output point cloud
  pub = nh.advertise<sensor_msgs::PointCloud2> ("cloud_publish_by_C", 100);
  pub2 = nh.advertise<UR3e_RG2_ER5_vision::UR3Msg> ("Object_Of_Interested", 100);
  markers_pub_ = nh.advertise<visualization_msgs::MarkerArray> ("msg_marker", 100);
    ros::spin();
  ros::spin ();
}