#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

RPM = 60

def talker():
    pub = rospy.Publisher("rpm", Float32, queue_size=10)
    rospy.init_node("rpm_pub_node", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = RPM
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInitException:
        pass

