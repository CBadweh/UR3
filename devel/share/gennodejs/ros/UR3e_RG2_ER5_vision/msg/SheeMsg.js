// Auto-generated. Do not edit!

// (in-package UR3e_RG2_ER5_vision.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class SheeMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.hey_name = null;
      this.hey_age = null;
    }
    else {
      if (initObj.hasOwnProperty('hey_name')) {
        this.hey_name = initObj.hey_name
      }
      else {
        this.hey_name = '';
      }
      if (initObj.hasOwnProperty('hey_age')) {
        this.hey_age = initObj.hey_age
      }
      else {
        this.hey_age = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SheeMsg
    // Serialize message field [hey_name]
    bufferOffset = _serializer.string(obj.hey_name, buffer, bufferOffset);
    // Serialize message field [hey_age]
    bufferOffset = _serializer.uint8(obj.hey_age, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SheeMsg
    let len;
    let data = new SheeMsg(null);
    // Deserialize message field [hey_name]
    data.hey_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [hey_age]
    data.hey_age = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.hey_name);
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'UR3e_RG2_ER5_vision/SheeMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1044e1e78017b18872c4953bd0e40998';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string hey_name
    uint8 hey_age
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SheeMsg(null);
    if (msg.hey_name !== undefined) {
      resolved.hey_name = msg.hey_name;
    }
    else {
      resolved.hey_name = ''
    }

    if (msg.hey_age !== undefined) {
      resolved.hey_age = msg.hey_age;
    }
    else {
      resolved.hey_age = 0
    }

    return resolved;
    }
};

module.exports = SheeMsg;
