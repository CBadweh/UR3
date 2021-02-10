# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "UR3e_RG2_ER5_vision: 1 messages, 0 services")

set(MSG_I_FLAGS "-IUR3e_RG2_ER5_vision:/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_custom_target(_UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "UR3e_RG2_ER5_vision" "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" "geometry_msgs/Point:geometry_msgs/Pose:geometry_msgs/Quaternion"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(UR3e_RG2_ER5_vision
  "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/UR3e_RG2_ER5_vision
)

### Generating Services

### Generating Module File
_generate_module_cpp(UR3e_RG2_ER5_vision
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/UR3e_RG2_ER5_vision
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages UR3e_RG2_ER5_vision_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages_cpp _UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(UR3e_RG2_ER5_vision_gencpp)
add_dependencies(UR3e_RG2_ER5_vision_gencpp UR3e_RG2_ER5_vision_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS UR3e_RG2_ER5_vision_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(UR3e_RG2_ER5_vision
  "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/UR3e_RG2_ER5_vision
)

### Generating Services

### Generating Module File
_generate_module_eus(UR3e_RG2_ER5_vision
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/UR3e_RG2_ER5_vision
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages UR3e_RG2_ER5_vision_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages_eus _UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(UR3e_RG2_ER5_vision_geneus)
add_dependencies(UR3e_RG2_ER5_vision_geneus UR3e_RG2_ER5_vision_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS UR3e_RG2_ER5_vision_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(UR3e_RG2_ER5_vision
  "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/UR3e_RG2_ER5_vision
)

### Generating Services

### Generating Module File
_generate_module_lisp(UR3e_RG2_ER5_vision
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/UR3e_RG2_ER5_vision
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages UR3e_RG2_ER5_vision_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages_lisp _UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(UR3e_RG2_ER5_vision_genlisp)
add_dependencies(UR3e_RG2_ER5_vision_genlisp UR3e_RG2_ER5_vision_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS UR3e_RG2_ER5_vision_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(UR3e_RG2_ER5_vision
  "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/UR3e_RG2_ER5_vision
)

### Generating Services

### Generating Module File
_generate_module_nodejs(UR3e_RG2_ER5_vision
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/UR3e_RG2_ER5_vision
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages UR3e_RG2_ER5_vision_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages_nodejs _UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(UR3e_RG2_ER5_vision_gennodejs)
add_dependencies(UR3e_RG2_ER5_vision_gennodejs UR3e_RG2_ER5_vision_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS UR3e_RG2_ER5_vision_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(UR3e_RG2_ER5_vision
  "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/UR3e_RG2_ER5_vision
)

### Generating Services

### Generating Module File
_generate_module_py(UR3e_RG2_ER5_vision
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/UR3e_RG2_ER5_vision
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(UR3e_RG2_ER5_vision_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages UR3e_RG2_ER5_vision_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/UR3e_RG2_ER5_vision/msg/UR3Msg.msg" NAME_WE)
add_dependencies(UR3e_RG2_ER5_vision_generate_messages_py _UR3e_RG2_ER5_vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(UR3e_RG2_ER5_vision_genpy)
add_dependencies(UR3e_RG2_ER5_vision_genpy UR3e_RG2_ER5_vision_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS UR3e_RG2_ER5_vision_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/UR3e_RG2_ER5_vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/UR3e_RG2_ER5_vision
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/UR3e_RG2_ER5_vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/UR3e_RG2_ER5_vision
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/UR3e_RG2_ER5_vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/UR3e_RG2_ER5_vision
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/UR3e_RG2_ER5_vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/UR3e_RG2_ER5_vision
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/UR3e_RG2_ER5_vision)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/UR3e_RG2_ER5_vision\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/UR3e_RG2_ER5_vision
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(UR3e_RG2_ER5_vision_generate_messages_py std_msgs_generate_messages_py)
endif()
