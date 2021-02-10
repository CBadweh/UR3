;; Auto-generated. Do not edit!


(when (boundp 'UR3e_RG2_ER5_vision::SheeMsg)
  (if (not (find-package "UR3E_RG2_ER5_VISION"))
    (make-package "UR3E_RG2_ER5_VISION"))
  (shadow 'SheeMsg (find-package "UR3E_RG2_ER5_VISION")))
(unless (find-package "UR3E_RG2_ER5_VISION::SHEEMSG")
  (make-package "UR3E_RG2_ER5_VISION::SHEEMSG"))

(in-package "ROS")
;;//! \htmlinclude SheeMsg.msg.html


(defclass UR3e_RG2_ER5_vision::SheeMsg
  :super ros::object
  :slots (_hey_name _hey_age ))

(defmethod UR3e_RG2_ER5_vision::SheeMsg
  (:init
   (&key
    ((:hey_name __hey_name) "")
    ((:hey_age __hey_age) 0)
    )
   (send-super :init)
   (setq _hey_name (string __hey_name))
   (setq _hey_age (round __hey_age))
   self)
  (:hey_name
   (&optional __hey_name)
   (if __hey_name (setq _hey_name __hey_name)) _hey_name)
  (:hey_age
   (&optional __hey_age)
   (if __hey_age (setq _hey_age __hey_age)) _hey_age)
  (:serialization-length
   ()
   (+
    ;; string _hey_name
    4 (length _hey_name)
    ;; uint8 _hey_age
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _hey_name
       (write-long (length _hey_name) s) (princ _hey_name s)
     ;; uint8 _hey_age
       (write-byte _hey_age s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _hey_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _hey_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _hey_age
     (setq _hey_age (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get UR3e_RG2_ER5_vision::SheeMsg :md5sum-) "1044e1e78017b18872c4953bd0e40998")
(setf (get UR3e_RG2_ER5_vision::SheeMsg :datatype-) "UR3e_RG2_ER5_vision/SheeMsg")
(setf (get UR3e_RG2_ER5_vision::SheeMsg :definition-)
      "string hey_name
uint8 hey_age
")



(provide :UR3e_RG2_ER5_vision/SheeMsg "1044e1e78017b18872c4953bd0e40998")


