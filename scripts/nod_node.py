#!/usr/bin/env python

#from sound_play.libsoundplay import SoundClient
#from sound_play.msg import SoundRequest
#from std_msgs.msg import String
#import rospy
import rospy
from pr2_controllers_msgs.msg import PointHeadAction
from pr2_controllers_msgs.msg import PointHeadGoal
from std_msgs.msg import Empty
from geometry_msgs.msg import PointStamped

class Head(object):
    def __init__(self):
        self._action_client = actionlib.SimpleActionClient("/head_traj_controller/point_head_action"
                                                            pr2_controllers_msgs.msg.PointHeadAction)
    def lookAt(frame_id, x, y, z): 
        #nod function calls lookAt twice
        self._action_client.wait_for_server()
        goal = PointHeadGoal()

        point = PointStamped()
        #frame_id is brought in as an argument
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
        #Check the formatting of min_duration!
        goal.min_duration = ros.Duration(0.5)
        goal.max_velocity = 1.0

        #send the goal
        self._action_client.send_goal(goal)
        #wait for result
        self._action_client.wait_for_result()
        #get the result...?
        return self._action_client.get_result()


    def nod(int n):
        count = 0;
        while (ros.ok() && count < n):
            #PR2 is about 1.25 m high?
            #looks out and up
            lookAt("base_link", 3.0, 0.0, 2.0)
            #looks out and down
            lookAt("base_link", 3.0, 0.0, 0.5)
            count += 1

def main():
    #Naming the node: same as file? Specific?
    rospy.init_node('head_nod_node')
    head = Head()
    rospy.Subscriber('nod', Empty, head.nod)
    rospy.spin()
    #How do you use Subscriber? I want to use nodHead(with an int)
    
#def main():
#    rospy.init_node('sound_play_tts')
#    sound_handle = SoundClient()
#    voice = 'voice_kal_diphone'
#    speaker = Speaker(sound_handle, voice)
#    rospy.Subscriber('text_to_speech', String, speaker.speak)
#    rospy.spin()

if __name__ == '__main__':
    main()
