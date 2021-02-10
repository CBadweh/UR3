; Auto-generated. Do not edit!


(cl:in-package UR3e_RG2_ER5_vision-msg)


;//! \htmlinclude UR3Msg.msg.html

(cl:defclass <UR3Msg> (roslisp-msg-protocol:ros-message)
  ((Obj_name
    :reader Obj_name
    :initarg :Obj_name
    :type cl:string
    :initform "")
   (Obj_Pose
    :reader Obj_Pose
    :initarg :Obj_Pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (Radius
    :reader Radius
    :initarg :Radius
    :type cl:float
    :initform 0.0))
)

(cl:defclass UR3Msg (<UR3Msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UR3Msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UR3Msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name UR3e_RG2_ER5_vision-msg:<UR3Msg> is deprecated: use UR3e_RG2_ER5_vision-msg:UR3Msg instead.")))

(cl:ensure-generic-function 'Obj_name-val :lambda-list '(m))
(cl:defmethod Obj_name-val ((m <UR3Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader UR3e_RG2_ER5_vision-msg:Obj_name-val is deprecated.  Use UR3e_RG2_ER5_vision-msg:Obj_name instead.")
  (Obj_name m))

(cl:ensure-generic-function 'Obj_Pose-val :lambda-list '(m))
(cl:defmethod Obj_Pose-val ((m <UR3Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader UR3e_RG2_ER5_vision-msg:Obj_Pose-val is deprecated.  Use UR3e_RG2_ER5_vision-msg:Obj_Pose instead.")
  (Obj_Pose m))

(cl:ensure-generic-function 'Radius-val :lambda-list '(m))
(cl:defmethod Radius-val ((m <UR3Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader UR3e_RG2_ER5_vision-msg:Radius-val is deprecated.  Use UR3e_RG2_ER5_vision-msg:Radius instead.")
  (Radius m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UR3Msg>) ostream)
  "Serializes a message object of type '<UR3Msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'Obj_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'Obj_name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Obj_Pose) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Radius))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UR3Msg>) istream)
  "Deserializes a message object of type '<UR3Msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Obj_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'Obj_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Obj_Pose) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Radius) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UR3Msg>)))
  "Returns string type for a message object of type '<UR3Msg>"
  "UR3e_RG2_ER5_vision/UR3Msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UR3Msg)))
  "Returns string type for a message object of type 'UR3Msg"
  "UR3e_RG2_ER5_vision/UR3Msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UR3Msg>)))
  "Returns md5sum for a message object of type '<UR3Msg>"
  "58d1707d0143a3a0da3fcde7e0164d11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UR3Msg)))
  "Returns md5sum for a message object of type 'UR3Msg"
  "58d1707d0143a3a0da3fcde7e0164d11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UR3Msg>)))
  "Returns full string definition for message of type '<UR3Msg>"
  (cl:format cl:nil "string Obj_name~%geometry_msgs/Pose Obj_Pose~%float64 Radius~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UR3Msg)))
  "Returns full string definition for message of type 'UR3Msg"
  (cl:format cl:nil "string Obj_name~%geometry_msgs/Pose Obj_Pose~%float64 Radius~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UR3Msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'Obj_name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Obj_Pose))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UR3Msg>))
  "Converts a ROS message object to a list"
  (cl:list 'UR3Msg
    (cl:cons ':Obj_name (Obj_name msg))
    (cl:cons ':Obj_Pose (Obj_Pose msg))
    (cl:cons ':Radius (Radius msg))
))
