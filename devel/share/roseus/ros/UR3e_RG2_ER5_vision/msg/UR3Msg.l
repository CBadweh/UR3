;; Auto-generated. Do not edit!


(when (boundp 'UR3e_RG2_ER5_vision::UR3Msg)
  (if (not (find-package "UR3E_RG2_ER5_VISION"))
    (make-package "UR3E_RG2_ER5_VISION"))
  (shadow 'UR3Msg (find-package "UR3E_RG2_ER5_VISION")))
(unless (find-package "UR3E_RG2_ER5_VISION::UR3MSG")
  (make-package "UR3E_RG2_ER5_VISION::UR3MSG"))

(in-package "ROS")
;;//! \htmlinclude UR3Msg.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass UR3e_RG2_ER5_vision::UR3Msg
  :super ros::object
  :slots (_Obj_name _Obj_Pose _Radius ))

(defmethod UR3e_RG2_ER5_vision::UR3Msg
  (:init
   (&key
    ((:Obj_name __Obj_name) "")
    ((:Obj_Pose __Obj_Pose) (instance geometry_msgs::Pose :init))
    ((:Radius __Radius) 0.0)
    )
   (send-super :init)
   (setq _Obj_name (string __Obj_name))
   (setq _Obj_Pose __Obj_Pose)
   (setq _Radius (float __Radius))
   self)
  (:Obj_name
   (&optional __Obj_name)
   (if __Obj_name (setq _Obj_name __Obj_name)) _Obj_name)
  (:Obj_Pose
   (&rest __Obj_Pose)
   (if (keywordp (car __Obj_Pose))
       (send* _Obj_Pose __Obj_Pose)
     (progn
       (if __Obj_Pose (setq _Obj_Pose (car __Obj_Pose)))
       _Obj_Pose)))
  (:Radius
   (&optional __Radius)
   (if __Radius (setq _Radius __Radius)) _Radius)
  (:serialization-length
   ()
   (+
    ;; string _Obj_name
    4 (length _Obj_name)
    ;; geometry_msgs/Pose _Obj_Pose
    (send _Obj_Pose :serialization-length)
    ;; float64 _Radius
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _Obj_name
       (write-long (length _Obj_name) s) (princ _Obj_name s)
     ;; geometry_msgs/Pose _Obj_Pose
       (send _Obj_Pose :serialize s)
     ;; float64 _Radius
       (sys::poke _Radius (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _Obj_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _Obj_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Pose _Obj_Pose
     (send _Obj_Pose :deserialize buf ptr-) (incf ptr- (send _Obj_Pose :serialization-length))
   ;; float64 _Radius
     (setq _Radius (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get UR3e_RG2_ER5_vision::UR3Msg :md5sum-) "58d1707d0143a3a0da3fcde7e0164d11")
(setf (get UR3e_RG2_ER5_vision::UR3Msg :datatype-) "UR3e_RG2_ER5_vision/UR3Msg")
(setf (get UR3e_RG2_ER5_vision::UR3Msg :definition-)
      "string Obj_name
geometry_msgs/Pose Obj_Pose
float64 Radius
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :UR3e_RG2_ER5_vision/UR3Msg "58d1707d0143a3a0da3fcde7e0164d11")


