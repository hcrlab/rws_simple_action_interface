#!/usr/bin/env python

import rospy
import dynamic_reconfigure.client
from std_msgs.msg import Empty

class Laser(object):
    def __init__(self):
        self.client = dynamic_reconfigure.client.Client('camera_synchronizer_node')

    def on(self, msg):
    	params = { 'narrow_stereo_trig_mode' : 3 }
    	self.client.update_configuration(params)

    def off(self,msg):
    	params2 = { 'narrow_stereo_trig_mode' : 4 }
    	self.client.update_configuration(params2)
        

def main():
	rospy.init_node('laser_node')
	laser = Laser()
	rospy.Subscriber('laser_ON', Empty, laser.on)
	rospy.Subscriber('laser_OFF', Empty, laser.off)
	rospy.spin()


if __name__ == '__main__':
    main()
