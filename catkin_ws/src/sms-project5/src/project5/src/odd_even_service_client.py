#!/usr/bin/env python

import rospy
from project5.srv import OddEvenCheck, OddEvenCheckResponse

def determineOddEven(req):
    remainder = req.number % 2

    if remainder == 0:
        return OddEvenCheckResponse("Even")
    elif remainder == 1:
        return OddEvenCheckResponse("Odd")
    else:
        return OddEvenCheckResponse("Invalid input")

def main():
    rospy.init_node('odd_even_service_client_node')
    rospy.wait_for_service('odd_even_check')
    client = rospy.ServiceProxy('odd_even_check', OddEvenCheck)
    
    while not rospy.is_shutdown():
        try:
            input_num = int(input("Enter an integer (0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if input_num == 0:
            print("Exiting Application...")
            return
        
        resp = client(input_num)
        print("The number is {}".format(resp.answer))

if __name__ == '__main__':
    main()
