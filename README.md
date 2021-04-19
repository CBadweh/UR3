# UR3
# For launch world
$roscd UR3e_RG2_ER5_vision

$roslaunch UR3e_RG2_ER5_description gazebo.launch gui:=false

$rosrun rviz rviz -d rviz.rviz


# For adding or removing object in gazebo
$roscd UR3e_RG2_ER5_vision

$rosrun gazebo_ros spawn_model -file ./box.urdf -urdf -z 1 -model my_model

$rosservice call /gazebo/delete_model "model_name: 'my_model'" 


# For calcuating object's distace and size using point cloud

$roscd UR3e_RG2_ER5_vision

$roslaunch UR3e_RG2_ER5_vision pcl_Background_subtraction.launch

$rosrun UR3e_RG2_ER5_vision PLC_pipeline


# For calculating object's color and sift using OpenCV 

$roscd UR3e_RG2_ER5_vision

$rosrun UR3e_RG2_ER5_vision Background_Subtraction_node.py

$rosrun UR3e_RG2_ER5_vision OpenCV_BGS_Color_SIFT_7th.py

