; Auto-generated. Do not edit!


(cl:in-package test_pkg-msg)


;//! \htmlinclude customMessage.msg.html

(cl:defclass <customMessage> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (value
    :reader value
    :initarg :value
    :type cl:float
    :initform 0.0))
)

(cl:defclass customMessage (<customMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <customMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'customMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_pkg-msg:<customMessage> is deprecated: use test_pkg-msg:customMessage instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <customMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_pkg-msg:name-val is deprecated.  Use test_pkg-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <customMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_pkg-msg:value-val is deprecated.  Use test_pkg-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <customMessage>) ostream)
  "Serializes a message object of type '<customMessage>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <customMessage>) istream)
  "Deserializes a message object of type '<customMessage>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'value) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<customMessage>)))
  "Returns string type for a message object of type '<customMessage>"
  "test_pkg/customMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'customMessage)))
  "Returns string type for a message object of type 'customMessage"
  "test_pkg/customMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<customMessage>)))
  "Returns md5sum for a message object of type '<customMessage>"
  "db3486341a840969e8845548decf6f11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'customMessage)))
  "Returns md5sum for a message object of type 'customMessage"
  "db3486341a840969e8845548decf6f11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<customMessage>)))
  "Returns full string definition for message of type '<customMessage>"
  (cl:format cl:nil "# CustomMessage.msg~%string name~%float32 value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'customMessage)))
  "Returns full string definition for message of type 'customMessage"
  (cl:format cl:nil "# CustomMessage.msg~%string name~%float32 value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <customMessage>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <customMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'customMessage
    (cl:cons ':name (name msg))
    (cl:cons ':value (value msg))
))
