#!/usr/bin/env python

import rospy
from project5.srv import OddEvenCheck, OddEvenCheckResponse


def determineOddEven(req):
    remainder = req.number % 2

    if remainder == 0:
        answer = "Even"
    elif remainder == 1:
        answer = "Odd"
    else:
        return False

    return OddEvenCheckResponse(answer)


def main():
    rospy.init_node('odd_even_service_server_node')

    service = rospy.Service('odd_even_check', OddEvenCheck, determineOddEven)

    rospy.loginfo("Odd Even Check Server Running...")

    rospy.spin()


if __name__ == '__main__':
    main()
