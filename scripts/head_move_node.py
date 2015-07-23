#!/usr/bin/env python

from pr2_controllers_msgs.msg import PointHeadAction, PointHeadGoal
from std_msgs.msg import Empty
import rospy

class Head(object):
    def __init__(self, sound_handle, voice):
        self._sound_handle = sound_handle
        self._voice = voice
        self._action_client = actionlib.SimpleActionClient("/head_traj_controller/point_head_action", 
                                                            pr2_controllers_msgs.msg.PointHeadAction)
        
    def nod(self, msg):
        # Waits until the action server has started up and started
        # listening for goals.
        self._action_client.wait_for_server()
    
        # Creates a goal to send to the action server.
        goal = PointHeadGoal()
        
        #Fill in goal somehow
    
        # Sends the goal to the action server.
        self._action_client.send_goal(goal)
    
        # Waits for the server to finish performing the action.
        self._action_client.wait_for_result()
    
        # Prints out the result of executing the action
        return self._action_client.get_result() 
        
    
def main():
    rospy.init_node('head_nod_node')
    head = Head()
    rospy.Subscriber('nod', Empty, head.nod)
    rospy.spin()

if __name__ == '__main__':
    main()
