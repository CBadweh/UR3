cmake_minimum_required(VERSION 2.8.3)
project(UR3e_RG2_ER5_vision)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)
#catkin_package()
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
  pcl_ros

)


add_message_files(
  FILES
  UR3Msg.msg
  UR3CV.msg
  UR3Numpy.msg
  UR3CVKeypoints.msg
  UR3CVKeypointsVector.msg

)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(

	CATKIN_DEPENDS message_runtime
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  #added folder 
  #/usr/include/pcl-1.8  
  #/usr/include/eigen3
  /home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg
)


add_executable(PCL_subscriber src/PCL_subscriber.cpp)
add_dependencies(PCL_subscriber UR3e_RG2_ER5_vision_generate_messages_cpp)
target_link_libraries(PCL_subscriber ${catkin_LIBRARIES} ${PCL_LIBRARIES})

add_executable(PCL_publisher src/PCL_publisher.cpp)
add_dependencies(PCL_publisher UR3e_RG2_ER5_vision_generate_messages_cpp)
target_link_libraries(PCL_publisher ${catkin_LIBRARIES} ${PCL_LIBRARIES})

#add_executable(PCL_Visualizer src/PCL_Visualizer.cpp)
#target_link_libraries(PCL_Visualizer ${catkin_LIBRARIES})
#add_dependencies(PCL_Visualizer ${catkin_LIBRARIES} ${PCL_LIBRARIES})


add_executable(publisher_subscriber_demo src/publisher_subscriber_demo.cpp)
target_link_libraries(publisher_subscriber_demo ${catkin_LIBRARIES})
add_dependencies(publisher_subscriber_demo ${catkin_LIBRARIES} ${PCL_LIBRARIES})

add_executable(PLC_pipeline src/PLC_pipeline.cpp)
target_link_libraries(PLC_pipeline ${catkin_LIBRARIES})
add_dependencies(PLC_pipeline ${catkin_LIBRARIES} ${PCL_LIBRARIES})


