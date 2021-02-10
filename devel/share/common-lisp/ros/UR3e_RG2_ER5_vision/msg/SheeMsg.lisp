; Auto-generated. Do not edit!


(cl:in-package UR3e_RG2_ER5_vision-msg)


;//! \htmlinclude SheeMsg.msg.html

(cl:defclass <SheeMsg> (roslisp-msg-protocol:ros-message)
  ((hey_name
    :reader hey_name
    :initarg :hey_name
    :type cl:string
    :initform "")
   (hey_age
    :reader hey_age
    :initarg :hey_age
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SheeMsg (<SheeMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SheeMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SheeMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name UR3e_RG2_ER5_vision-msg:<SheeMsg> is deprecated: use UR3e_RG2_ER5_vision-msg:SheeMsg instead.")))

(cl:ensure-generic-function 'hey_name-val :lambda-list '(m))
(cl:defmethod hey_name-val ((m <SheeMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader UR3e_RG2_ER5_vision-msg:hey_name-val is deprecated.  Use UR3e_RG2_ER5_vision-msg:hey_name instead.")
  (hey_name m))

(cl:ensure-generic-function 'hey_age-val :lambda-list '(m))
(cl:defmethod hey_age-val ((m <SheeMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader UR3e_RG2_ER5_vision-msg:hey_age-val is deprecated.  Use UR3e_RG2_ER5_vision-msg:hey_age instead.")
  (hey_age m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SheeMsg>) ostream)
  "Serializes a message object of type '<SheeMsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'hey_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'hey_name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hey_age)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SheeMsg>) istream)
  "Deserializes a message object of type '<SheeMsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'hey_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'hey_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hey_age)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SheeMsg>)))
  "Returns string type for a message object of type '<SheeMsg>"
  "UR3e_RG2_ER5_vision/SheeMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SheeMsg)))
  "Returns string type for a message object of type 'SheeMsg"
  "UR3e_RG2_ER5_vision/SheeMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SheeMsg>)))
  "Returns md5sum for a message object of type '<SheeMsg>"
  "1044e1e78017b18872c4953bd0e40998")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SheeMsg)))
  "Returns md5sum for a message object of type 'SheeMsg"
  "1044e1e78017b18872c4953bd0e40998")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SheeMsg>)))
  "Returns full string definition for message of type '<SheeMsg>"
  (cl:format cl:nil "string hey_name~%uint8 hey_age~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SheeMsg)))
  "Returns full string definition for message of type 'SheeMsg"
  (cl:format cl:nil "string hey_name~%uint8 hey_age~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SheeMsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'hey_name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SheeMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'SheeMsg
    (cl:cons ':hey_name (hey_name msg))
    (cl:cons ':hey_age (hey_age msg))
))
