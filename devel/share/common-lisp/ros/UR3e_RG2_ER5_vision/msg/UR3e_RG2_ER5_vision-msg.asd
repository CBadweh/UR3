
(cl:in-package :asdf)

(defsystem "UR3e_RG2_ER5_vision-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "UR3Msg" :depends-on ("_package_UR3Msg"))
    (:file "_package_UR3Msg" :depends-on ("_package"))
  ))