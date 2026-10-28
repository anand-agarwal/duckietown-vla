#!/bin/bash

source /environment.sh

dt-launchfile-init

rosrun drivevla_bridge camera_check_node.py

dt-launchfile-join
