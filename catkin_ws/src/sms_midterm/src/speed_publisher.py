#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def speed_publisher():
    pub = rospy.Publisher('vehicle_speed', Float32, queue_size=10)
    rospy.init_node('speed_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    while not rospy.is_shutdown():
        speed = 90 # Example speed in km/h
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_publisher()
    except rospy.ROSInterruptException:
        pass
