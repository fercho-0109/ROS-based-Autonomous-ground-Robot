// Auto-generated. Do not edit!

// (in-package test_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TimerGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.duration_time = null;
    }
    else {
      if (initObj.hasOwnProperty('duration_time')) {
        this.duration_time = initObj.duration_time
      }
      else {
        this.duration_time = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TimerGoal
    // Serialize message field [duration_time]
    bufferOffset = _serializer.float32(obj.duration_time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TimerGoal
    let len;
    let data = new TimerGoal(null);
    // Deserialize message field [duration_time]
    data.duration_time = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test_pkg/TimerGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '790a1b2f6126e5c09420d2652f44280f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Timer.action
    float32 duration_time # goal
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TimerGoal(null);
    if (msg.duration_time !== undefined) {
      resolved.duration_time = msg.duration_time;
    }
    else {
      resolved.duration_time = 0.0
    }

    return resolved;
    }
};

module.exports = TimerGoal;
