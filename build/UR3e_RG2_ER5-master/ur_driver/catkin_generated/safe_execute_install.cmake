execute_process(COMMAND "/home/cbadweh/UR3/build/UR3e_RG2_ER5-master/ur_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/cbadweh/UR3/build/UR3e_RG2_ER5-master/ur_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
