
(cl:in-package :asdf)

(defsystem "test_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WordCount" :depends-on ("_package_WordCount"))
    (:file "_package_WordCount" :depends-on ("_package"))
  ))