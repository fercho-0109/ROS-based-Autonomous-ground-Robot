
(cl:in-package :asdf)

(defsystem "test_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TimerAction" :depends-on ("_package_TimerAction"))
    (:file "_package_TimerAction" :depends-on ("_package"))
    (:file "TimerActionFeedback" :depends-on ("_package_TimerActionFeedback"))
    (:file "_package_TimerActionFeedback" :depends-on ("_package"))
    (:file "TimerActionGoal" :depends-on ("_package_TimerActionGoal"))
    (:file "_package_TimerActionGoal" :depends-on ("_package"))
    (:file "TimerActionResult" :depends-on ("_package_TimerActionResult"))
    (:file "_package_TimerActionResult" :depends-on ("_package"))
    (:file "TimerFeedback" :depends-on ("_package_TimerFeedback"))
    (:file "_package_TimerFeedback" :depends-on ("_package"))
    (:file "TimerGoal" :depends-on ("_package_TimerGoal"))
    (:file "_package_TimerGoal" :depends-on ("_package"))
    (:file "TimerResult" :depends-on ("_package_TimerResult"))
    (:file "_package_TimerResult" :depends-on ("_package"))
    (:file "customMessage" :depends-on ("_package_customMessage"))
    (:file "_package_customMessage" :depends-on ("_package"))
  ))