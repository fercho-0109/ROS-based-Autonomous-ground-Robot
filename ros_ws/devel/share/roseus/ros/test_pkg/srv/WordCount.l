;; Auto-generated. Do not edit!


(when (boundp 'test_pkg::WordCount)
  (if (not (find-package "TEST_PKG"))
    (make-package "TEST_PKG"))
  (shadow 'WordCount (find-package "TEST_PKG")))
(unless (find-package "TEST_PKG::WORDCOUNT")
  (make-package "TEST_PKG::WORDCOUNT"))
(unless (find-package "TEST_PKG::WORDCOUNTREQUEST")
  (make-package "TEST_PKG::WORDCOUNTREQUEST"))
(unless (find-package "TEST_PKG::WORDCOUNTRESPONSE")
  (make-package "TEST_PKG::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass test_pkg::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod test_pkg::WordCountRequest
  (:init
   (&key
    ((:words __words) "")
    )
   (send-super :init)
   (setq _words (string __words))
   self)
  (:words
   (&optional __words)
   (if __words (setq _words __words)) _words)
  (:serialization-length
   ()
   (+
    ;; string _words
    4 (length _words)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _words
       (write-long (length _words) s) (princ _words s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _words
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _words (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass test_pkg::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod test_pkg::WordCountResponse
  (:init
   (&key
    ((:count __count) 0)
    )
   (send-super :init)
   (setq _count (round __count))
   self)
  (:count
   (&optional __count)
   (if __count (setq _count __count)) _count)
  (:serialization-length
   ()
   (+
    ;; uint32 _count
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _count
       (write-long _count s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _count
     (setq _count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass test_pkg::WordCount
  :super ros::object
  :slots ())

(setf (get test_pkg::WordCount :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get test_pkg::WordCount :datatype-) "test_pkg/WordCount")
(setf (get test_pkg::WordCount :request) test_pkg::WordCountRequest)
(setf (get test_pkg::WordCount :response) test_pkg::WordCountResponse)

(defmethod test_pkg::WordCountRequest
  (:response () (instance test_pkg::WordCountResponse :init)))

(setf (get test_pkg::WordCountRequest :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get test_pkg::WordCountRequest :datatype-) "test_pkg/WordCountRequest")
(setf (get test_pkg::WordCountRequest :definition-)
      "# WordCount.srv
string words #input
---
uint32 count #output

")

(setf (get test_pkg::WordCountResponse :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get test_pkg::WordCountResponse :datatype-) "test_pkg/WordCountResponse")
(setf (get test_pkg::WordCountResponse :definition-)
      "# WordCount.srv
string words #input
---
uint32 count #output

")



(provide :test_pkg/WordCount "58903d21a3264f3408d79ba79e9f7c7e")


