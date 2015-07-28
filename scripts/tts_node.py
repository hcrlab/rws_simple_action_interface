#!/usr/bin/env python

from sound_play.libsoundplay import SoundClient
from sound_play.msg import SoundRequest
from std_msgs.msg import String

import rospy

class Speaker(object):
    def __init__(self, sound_handle, voice):
        self._sound_handle = sound_handle
        self._voice = voice 
        
    def speak(self, msg):
        self._sound_handle.say(msg.data, self._voice)
    
def main():
    rospy.init_node('sound_play_tts')
    sound_handle = SoundClient()
    voice = 'voice_kal_diphone'
    speaker = Speaker(sound_handle, voice)
    rospy.Subscriber('text_to_speech', String, speaker.speak)
    
    rospy.spin()

if __name__ == '__main__':
    main()
