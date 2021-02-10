// Auto-generated. Do not edit!

// (in-package UR3e_RG2_ER5_vision.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class UR3Msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Obj_name = null;
      this.Obj_Pose = null;
      this.Radius = null;
    }
    else {
      if (initObj.hasOwnProperty('Obj_name')) {
        this.Obj_name = initObj.Obj_name
      }
      else {
        this.Obj_name = '';
      }
      if (initObj.hasOwnProperty('Obj_Pose')) {
        this.Obj_Pose = initObj.Obj_Pose
      }
      else {
        this.Obj_Pose = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('Radius')) {
        this.Radius = initObj.Radius
      }
      else {
        this.Radius = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type UR3Msg
    // Serialize message field [Obj_name]
    bufferOffset = _serializer.string(obj.Obj_name, buffer, bufferOffset);
    // Serialize message field [Obj_Pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.Obj_Pose, buffer, bufferOffset);
    // Serialize message field [Radius]
    bufferOffset = _serializer.float64(obj.Radius, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type UR3Msg
    let len;
    let data = new UR3Msg(null);
    // Deserialize message field [Obj_name]
    data.Obj_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [Obj_Pose]
    data.Obj_Pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [Radius]
    data.Radius = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.Obj_name);
    return length + 68;
  }

  static datatype() {
    // Returns string type for a message object
    return 'UR3e_RG2_ER5_vision/UR3Msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '58d1707d0143a3a0da3fcde7e0164d11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string Obj_name
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new UR3Msg(null);
    if (msg.Obj_name !== undefined) {
      resolved.Obj_name = msg.Obj_name;
    }
    else {
      resolved.Obj_name = ''
    }

    if (msg.Obj_Pose !== undefined) {
      resolved.Obj_Pose = geometry_msgs.msg.Pose.Resolve(msg.Obj_Pose)
    }
    else {
      resolved.Obj_Pose = new geometry_msgs.msg.Pose()
    }

    if (msg.Radius !== undefined) {
      resolved.Radius = msg.Radius;
    }
    else {
      resolved.Radius = 0.0
    }

    return resolved;
    }
};

module.exports = UR3Msg;
