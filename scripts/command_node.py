#!/usr/bin/env python

import rospy

from std_msgs.msg import String

class Command(object):
    def __init__(self):
        

    def filter(self, msg):
    	command = msg.data
        
        if "nod" in command.lower():
            return "nod"
        else if "shake" in command.lower():
            return "shake"

        

def main():
	rospy.init_node('command_node')
	commander = Command()
	rospy.Subscriber('command_filter', String, commander.command_filter)
	rospy.spin()


if __name__ == '__main__':
    main()
