#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def speed_callback(data):
    plate_number = "2407Bema"
    speed_limit = rospy.get_param("/speed_limit") # Get the speed limit parameter, default value is 50 km/h
    if data.data > speed_limit:
        rospy.loginfo("Plate number: %s, Speed: %f km/h, Over speed limit!", plate_number, data.data)
    else:
        rospy.loginfo("Plate number: %s, Speed: %f km/h", plate_number, data.data)

def plate_subscriber():
    rospy.init_node('plate_subscriber', anonymous=True)
    rospy.Subscriber('vehicle_speed', Float32, speed_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        plate_subscriber()
    except rospy.ROSInterruptException:
        pass
