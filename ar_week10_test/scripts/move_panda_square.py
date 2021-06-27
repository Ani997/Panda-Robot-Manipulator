#!/usr/bin/env python
import sys
import copy
import rospy
import time
import moveit_commander
import moveit_msgs.msg
from math import pi
from ar_week10_test.msg import square_size

def callback(data):
    try:
        # Definining the robot start configuration
        start_conf = [0, -pi / 4, 0, -pi / 2, 0, pi / 3, 0]

        # Move the robot to the start configuration
        group.go(start_conf, wait=True)

	# stop function ensures no residual movement by the robot
        group.stop()

        # initialise an array for the positions
        way_pts = []

        # get current group positions
        pos = group.get_current_pose().pose


        pos.position.y += data.size  # 1st move
        way_pts.append(copy.deepcopy(pos))
	
        pos.position.x += data.size  # 2nd move
        way_pts.append(copy.deepcopy(pos))

	pos.position.y -= data.size  # 3rd move
        way_pts.append(copy.deepcopy(pos))

        pos.position.x -= data.size  # 4th move
        way_pts.append(copy.deepcopy(pos))


        # Computing the path to follow on the cartesian space
        (plan,fraction) = group.compute_cartesian_path(way_pts,0.01,0.0)  

        # trajectory planning 
        disp_traj = moveit_msgs.msg.DisplayTrajectory()
        disp_traj.trajectory_start = robot.get_current_state()
        disp_traj.trajectory.append(plan)
        
        print '------------------- Preview of the Planned Trajectory -------------------'
        display_trajectory_publisher.publish(disp_traj)
        time.sleep(5)

        # Executing the planned trajectory
        print '------------------- Executing the Planned Trajectory -------------------'
        group.execute(plan, wait=True)

    except rospy.ServiceException, e:
        print("Service call failed: %s" % e)


def move_panda_square():
    # initialise a node
    rospy.init_node('move_panda_square', anonymous=True)

    # wait for service
    print '------------------- Waiting for square size -------------------'
    # subrscibe and send the recieved data to callback function
    rospy.Subscriber('size', square_size, callback)
    rospy.spin()


if __name__ == "__main__":
    # initialise robot commander
    robot = moveit_commander.RobotCommander()

    # initialise scene planning interface
    scene = moveit_commander.PlanningSceneInterface()

    # initialise move group commander
    group = moveit_commander.MoveGroupCommander('panda_arm')

    # initialise display trajectory publisher
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=0)
    move_panda_square()
