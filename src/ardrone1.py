#!/usr/bin/env python

import roslib; roslib.load_manifest('ardrone_tutorials')
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from drone_controller import BasicDroneController
from cv_bridge import CvBridge


class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback)

    self.count = 0
    self.x_old = 0.0
    self.y_old = 0.0

  def callback(self,data):
     
      if controller is not None:
  
        cv_image = self.bridge.imgmsg_to_cv2(data)
       

        image = cv_image*50.0 
        image = np.uint8(image)

        ret,image = cv2.threshold(image,35,255,cv2.THRESH_TOZERO)
        ret,image = cv2.threshold(image,140,255,cv2.THRESH_TOZERO_INV)
        
        image2 = image[60:380, 110:530] 

        ret,image3 = cv2.threshold(image2,15,255,cv2.THRESH_BINARY)

        mm2 = cv2.moments(image2)
        mm3 = cv2.moments(image3)

        if mm3['m00'] :
          avg_depth = mm2['m00'] * 255.0 / mm3['m00']
          cm_x = mm3['m10']  / mm3['m00']
          cm_y = mm3['m01']  / mm3['m00']

          x = ( cm_x - 210.0 ) / 320.0
          y = avg_depth / 50.0 - 1.5

          r = 1.0 * x + (x - self.x_old) * 32.0
          p = 1.0 * y + (y - self.y_old) * 32.0

          controller.SetCommand( r, -p, 0.0, 0.0)
 
          print self.count, cm_x, cm_y, avg_depth, r, p
          
          self.x_old = x
          self.y_old = y
        else:  
          controller.SetCommand( 0.0, 0.0, 0.0, 0.0)
          print 'zero'
       
        self.count += 1

        cv2.imshow("wnd", image2)
        cv2.waitKey(1)

if __name__=='__main__':
	import sys
	rospy.init_node('ardrone1')
        ic = image_converter()

        cv2.namedWindow("wnd",cv2.WINDOW_AUTOSIZE)
	controller = BasicDroneController()
        try:
          rospy.spin()
        except KeyboardInterrupt:
          print "Shutting down"
	
        rospy.signal_shutdown('Great Flying!')
	sys.exit(0)
