#!/bin/bash

REPOSITORY_NAME="$(basename "$(dirname -- "$( readlink -f -- "$0"; )")")"

docker run -it --rm \
--network=host \
--ipc=host --pid=host \
--env UID=$(id -u) \
--env GID=$(id -g) \
--device /dev/i2c-3:/dev/i2c-1 \
--volume ./ros_slope_estimator:/colcon_ws/src/ros_slope_estimator \
ghcr.io/rosblox/${REPOSITORY_NAME}:humble
