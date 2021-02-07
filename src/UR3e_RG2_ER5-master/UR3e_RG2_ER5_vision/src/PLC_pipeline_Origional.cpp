
// source: https://stackoverflow.com/questions/61589904/not-correct-orientation-of-the-obb-box

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






ros::Publisher pub, markers_pub_;

void cloud_cb(const sensor_msgs::PointCloud2::ConstPtr &msg){

    // Convert to pcl point cloud
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_msg (new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::fromROSMsg(*msg,*cloud_msg);
    //ROS_DEBUG("%s: new ponitcloud (%i,%i)(%zu)",_name.c_str(),cloud_msg->width,cloud_msg->height,cloud_msg->size());

    // // Filter cloud
    // pcl::PassThrough<pcl::PointXYZRGB> pass;
    // pass.setInputCloud(cloud_msg);
    // pass.setFilterFieldName ("y");
    // pass.setFilterLimits(0.001,10);
    // pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
    // pass.filter (*cloud);

    // // Get segmentation ready
    // pcl::ModelCoefficients::Ptr coefficients(new pcl::ModelCoefficients);
    // pcl::PointIndices::Ptr inliers(new pcl::PointIndices);
    // pcl::SACSegmentation<pcl::PointXYZRGB> seg;
    // pcl::ExtractIndices<pcl::PointXYZRGB> extract;
    // seg.setOptimizeCoefficients (true);
    // seg.setModelType (pcl::SACMODEL_PLANE);
    // seg.setMethodType (pcl::SAC_RANSAC);
    // seg.setDistanceThreshold(0.04);

    // // Create pointcloud to publish inliers
    // pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_pub(new pcl::PointCloud<pcl::PointXYZRGB>);
    

    //     // Fit a plane
    //     seg.setInputCloud(cloud);
    //     seg.segment(*inliers, *coefficients);

    //     // Check result
    //     if (inliers->indices.size() == 0)
    //        {
    //         ROS_WARN_STREAM ("Could not estimate a planar model for the given dataset.") ;
    //         }


    //     // Extract inliers
    //     extract.setInputCloud(cloud);
    //     extract.setIndices(inliers);
    //     extract.setNegative(true);
    //     //pcl::PointCloud<pcl::PointXYZRGB> cloudF;
    //     pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_box (new pcl::PointCloud<pcl::PointXYZRGB> ());
    //     extract.filter(*cloud_box);
       
  //Moment of Inertia
  pcl::MomentOfInertiaEstimation <pcl::PointXYZRGB> feature_extractor;
  // feature_extractor.setInputCloud (cloud_box); // Uncommend this if using the block abolve
  feature_extractor.setInputCloud (cloud_msg);
  feature_extractor.compute ();

  std::vector <float> moment_of_inertia;
  std::vector <float> eccentricity;

  pcl::PointXYZRGB min_point_OBB;
  pcl::PointXYZRGB max_point_OBB;
  pcl::PointXYZRGB position_OBB;
  Eigen::Matrix3f rotational_matrix_OBB;
  float major_value, middle_value, minor_value;
  Eigen::Vector3f major_vector, middle_vector, minor_vector;
  Eigen::Vector3f mass_center;

  feature_extractor.getMomentOfInertia (moment_of_inertia);
  feature_extractor.getEccentricity (eccentricity);
  feature_extractor.getOBB (min_point_OBB, max_point_OBB, position_OBB, rotational_matrix_OBB);
  feature_extractor.getEigenValues (major_value, middle_value, minor_value);
  feature_extractor.getEigenVectors (major_vector, middle_vector, minor_vector);
  feature_extractor.getMassCenter (mass_center);

  Eigen::Vector3f position (position_OBB.x, position_OBB.y, position_OBB.z);
  Eigen::Quaternionf quat (rotational_matrix_OBB);
   
  cout << " orientation x  = " << quat.x() <<  endl;
  cout << " orientation y = "  << quat.y() <<  endl;
  cout << " orientation z = "  << quat.z() <<  endl;
  cout << " orientation w = "  << quat.w() <<  endl;
  cout << " postion x  = " << position_OBB.x <<  endl;
  cout << " postion y  = " << position_OBB.y <<  endl;
  cout << " postion z  = " << position_OBB.z <<  endl;
   

    // Publish points
    sensor_msgs::PointCloud2 cloud_publish;
    pcl::toROSMsg(*cloud_msg,cloud_publish);
    pub.publish(cloud_publish);

  //Visualisation Marker;
  std::string ns; 
  float r; 
  float g; 
  float b;
  visualization_msgs::MarkerArray msg_marker;
  visualization_msgs::Marker bbx_marker;
  bbx_marker.header.frame_id = "kinect_optical_link";
  bbx_marker.header.stamp = ros::Time::now();
  bbx_marker.ns = ns;
  bbx_marker.type = visualization_msgs::Marker::CUBE;
  bbx_marker.action = visualization_msgs::Marker::ADD;
  bbx_marker.pose.position.x =  position_OBB.x;
  bbx_marker.pose.position.y =  position_OBB.y;
  bbx_marker.pose.position.z =  position_OBB.z;
  bbx_marker.pose.orientation.x = quat.x();
  bbx_marker.pose.orientation.y = quat.y();
  bbx_marker.pose.orientation.z = quat.z();
  bbx_marker.pose.orientation.w = quat.w();
  bbx_marker.scale.x = (max_point_OBB.x - min_point_OBB.x);
  bbx_marker.scale.y = (max_point_OBB.y - min_point_OBB.y);
  bbx_marker.scale.z = (max_point_OBB.z - min_point_OBB.z);
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
  ros::init (argc, argv, "my_pcl_tutorial");
  ros::NodeHandle nh;
  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe ("/extract_plane_indices/output", 200, cloud_cb);  //topic subscribe to
  // Create a ROS publisher for the output point cloud
  pub = nh.advertise<sensor_msgs::PointCloud2> ("cloud_publish_by_C", 100);
  markers_pub_ = nh.advertise<visualization_msgs::MarkerArray> ("msg_marker", 100);
    ros::spin();
  ros::spin ();
}