#!/usr/bin/env python

import rospy
from pr2_controllers_msgs.msg import PointHeadAction
from pr2_controllers_msgs.msg import PointHeadGoal
from std_msgs.msg import Empty, Int8
from geometry_msgs.msg import PointStamped
import actionlib

class Head(object):
    def __init__(self):
        self._action_client = actionlib.SimpleActionClient("/head_traj_controller/point_head_action",
                                                            PointHeadAction)
    def lookAt(self, frame_id, x, y, z): 
        self._action_client.wait_for_server()
        goal = PointHeadGoal()

        point = PointStamped()
        point.header.frame_id = frame_id
        point.point.x = x
        point.point.y = y
        point.point.z = z
        goal.target = point

        #pointing high-def camera frame
        goal.pointing_frame = "high_def_frame"
        goal.pointing_axis.x = 1
        goal.pointing_axis.y = 0
        goal.pointing_axis.z = 0
        goal.min_duration = rospy.Duration(0.5)
        goal.max_velocity = 1.0

        #send the goal
        self._action_client.send_goal(goal)
        #wait for result
        self._action_client.wait_for_result()
        #get the result...?
        return self._action_client.get_result()


    def nod(self, msg):
        count = 0
        while (not rospy.is_shutdown() and count < msg.data):
            #PR2 is about 1.25 m high?
            #looks out and up
            self.lookAt("base_link", 3.0, 0.0, 2.0)
            #looks out and down
            self.lookAt("base_link", 3.0, 0.0, 0.5)
            count += 1

    def shake(self, msg):
        count = 0
        while (not rospy.is_shutdown() and count < msg.data):
            self.lookAt("base_link", 3.0, 0.75, 1.25)
            self.lookAt("base_link", 3.0, -0.75, 1.25)
            count += 1

def main():
    rospy.init_node('head_nod_node')
    head = Head()
    rospy.Subscriber('nod', Int8, head.nod)
    rospy.Subscriber('shake', Int8, head.shake)
    rospy.spin()
    


if __name__ == '__main__':
    main()
