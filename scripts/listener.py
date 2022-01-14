#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import String

def callback(data):
    if (random.randint(0,25) < 5):
        input('たまには自分の頭使って計算せい（#^ω^）\n')
    else:
        rospy.loginfo(eval(data.data))
    
def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
