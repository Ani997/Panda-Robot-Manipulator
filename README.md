# Panda-Robot-Manipulator
Implement a ROS package which automatically generates Cartesian space movements of the end effector of the panda robot manipulator. The end-effector will sketch squares of varying sizes on the Cartesian plane.

To execute the simulation, please follow the given steps:
1) Download the zip file of the package into your catkin workspace.

2) Now, navigate to your catkin workspace directory through the terminal and issue the "catkin_make" command.

3) To install panda moveit repository, we issue the following commands after navigating to "catkin_ws/src" in the terminal.
          1] git clone -b melodic-devel https://github.com/ros-planning/panda_moveit_config.git
          2] rosdep update
          3] rosdep install --from-paths . --ignore-src -r -y
          4] cd ..
          5] catkin_make

4) In the "catkin_ws/src/ar_week10_test" directory we write the programs in the "scripts" folder and the message file in the "msg" folder.

5) To make our python programs executable, we navigate to the directory where they are stored through the terminal and issue the command "chmod +x program_name.py".

6) Now, we open four new terminal tabs and issue the following commands one by one:
            1] roslaunch panda_moveit_config demo.launch
            2] rosrun ar_week10_test square_size_generator.py
            3] rosrun ar_week10_test move_panda_square.py
            4] rosrun rqt_plot rqt_plot
