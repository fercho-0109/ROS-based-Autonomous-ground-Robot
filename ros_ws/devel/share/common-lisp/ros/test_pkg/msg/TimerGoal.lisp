; Auto-generated. Do not edit!


(cl:in-package test_pkg-msg)


;//! \htmlinclude TimerGoal.msg.html

(cl:defclass <TimerGoal> (roslisp-msg-protocol:ros-message)
  ((duration_time
    :reader duration_time
    :initarg :duration_time
    :type cl:float
    :initform 0.0))
)

(cl:defclass TimerGoal (<TimerGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TimerGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TimerGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_pkg-msg:<TimerGoal> is deprecated: use test_pkg-msg:TimerGoal instead.")))

(cl:ensure-generic-function 'duration_time-val :lambda-list '(m))
(cl:defmethod duration_time-val ((m <TimerGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_pkg-msg:duration_time-val is deprecated.  Use test_pkg-msg:duration_time instead.")
  (duration_time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TimerGoal>) ostream)
  "Serializes a message object of type '<TimerGoal>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'duration_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TimerGoal>) istream)
  "Deserializes a message object of type '<TimerGoal>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration_time) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TimerGoal>)))
  "Returns string type for a message object of type '<TimerGoal>"
  "test_pkg/TimerGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TimerGoal)))
  "Returns string type for a message object of type 'TimerGoal"
  "test_pkg/TimerGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TimerGoal>)))
  "Returns md5sum for a message object of type '<TimerGoal>"
  "790a1b2f6126e5c09420d2652f44280f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TimerGoal)))
  "Returns md5sum for a message object of type 'TimerGoal"
  "790a1b2f6126e5c09420d2652f44280f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TimerGoal>)))
  "Returns full string definition for message of type '<TimerGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Timer.action~%float32 duration_time # goal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TimerGoal)))
  "Returns full string definition for message of type 'TimerGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Timer.action~%float32 duration_time # goal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TimerGoal>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TimerGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'TimerGoal
    (cl:cons ':duration_time (duration_time msg))
))