#!/usr/bin/env python
import rospy
import numpy as np
from ar_week10_test.msg import square_size


def square_size_generator():
    # initialise new topic
    PUB = rospy.Publisher('size', square_size, queue_size=0)

    # initialise new node
    rospy.init_node('square_size_generator', anonymous=True)
    rate = rospy.Rate(0.05) # Publish values every 20 seconds
    msg = square_size()
    while not rospy.is_shutdown():
        msg.size = np.random.uniform(0.05, 0.20) # Define the values to be published
        rospy.loginfo(msg)
        PUB.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        square_size_generator()
    except rospy.ROSInterruptException:
        pass
