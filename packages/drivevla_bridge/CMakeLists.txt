cmake_minimum_required(VERSION 3.0.2)

project(drivevla_bridge)

find_package(catkin REQUIRED COMPONENTS
    rospy
    sensor_msgs
    geometry_msgs
    duckietown_msgs
    cv_bridge
)

catkin_package()

catkin_install_python(
    PROGRAMS
        src/camera_check_node.py
        src/cmd_gate_node.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
