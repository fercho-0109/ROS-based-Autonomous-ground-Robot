;; Auto-generated. Do not edit!


(when (boundp 'test_pkg::customMessage)
  (if (not (find-package "TEST_PKG"))
    (make-package "TEST_PKG"))
  (shadow 'customMessage (find-package "TEST_PKG")))
(unless (find-package "TEST_PKG::CUSTOMMESSAGE")
  (make-package "TEST_PKG::CUSTOMMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude customMessage.msg.html


(defclass test_pkg::customMessage
  :super ros::object
  :slots (_name _value ))

(defmethod test_pkg::customMessage
  (:init
   (&key
    ((:name __name) "")
    ((:value __value) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _value (float __value))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; float32 _value
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float32 _value
       (sys::poke _value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _value
     (setq _value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get test_pkg::customMessage :md5sum-) "db3486341a840969e8845548decf6f11")
(setf (get test_pkg::customMessage :datatype-) "test_pkg/customMessage")
(setf (get test_pkg::customMessage :definition-)
      "# CustomMessage.msg
string name
float32 value

")



(provide :test_pkg/customMessage "db3486341a840969e8845548decf6f11")


