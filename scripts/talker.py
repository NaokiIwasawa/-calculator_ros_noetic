#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
        str = input('計算式を入力してください：')
        pub.publish(str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass