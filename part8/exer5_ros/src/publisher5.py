#!/usr/bin/env python

from __future__ import print_function

from exer5_ros.srv import new_name, result
import rospy

def handle_add_two_ints(req):
    #print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return result(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', new_name, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

