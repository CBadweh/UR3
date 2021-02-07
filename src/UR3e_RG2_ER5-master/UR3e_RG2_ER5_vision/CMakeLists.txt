cmake_minimum_required(VERSION 2.8.3)
project(UR3e_RG2_ER5_vision)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)
catkin_package()
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  pcl_ros

)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES UR3e_RG2_ER5_description
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  #added folder 
  #/usr/include/pcl-1.8  
  #/usr/include/eigen3
)


add_executable(PCL_subscriber src/PCL_subscriber.cpp)
add_dependencies(PCL_subscriber UR3e_RG2_ER5_vision_generate_messages_cpp)
target_link_libraries(PCL_subscriber ${catkin_LIBRARIES} ${PCL_LIBRARIES})

#add_executable(PCL_Visualizer src/PCL_Visualizer.cpp)
#target_link_libraries(PCL_Visualizer ${catkin_LIBRARIES})
#add_dependencies(PCL_Visualizer ${catkin_LIBRARIES} ${PCL_LIBRARIES})


add_executable(publisher_subscriber_demo src/publisher_subscriber_demo.cpp)
target_link_libraries(publisher_subscriber_demo ${catkin_LIBRARIES})
add_dependencies(publisher_subscriber_demo ${catkin_LIBRARIES} ${PCL_LIBRARIES})

add_executable(PLC_pipeline src/PLC_pipeline.cpp)
target_link_libraries(PLC_pipeline ${catkin_LIBRARIES})
add_dependencies(PLC_pipeline ${catkin_LIBRARIES} ${PCL_LIBRARIES})


