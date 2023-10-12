#!/bin/bash

REPOSITORY_NAME="$(basename "$(dirname -- "$( readlink -f -- "$0"; )")")"

docker run -it --rm \
--network=host \
--ipc=host --pid=host \
--env UID=$(id -u) \
--env GID=$(id -g) \
--device /dev/i2c-3:/dev/i2c-1 \
--env ROS_DOMAIN_ID=23 \
--volume ./slope_estimation:/colcon_ws/src/slope_estimation \
--volume ./slope_estimation_interfaces:/colcon_ws/src/slope_estimation_interfaces \
ghcr.io/rosblox/${REPOSITORY_NAME}:humble
