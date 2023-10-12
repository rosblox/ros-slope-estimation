ARG ROS_DISTRO

FROM ros:${ROS_DISTRO}-ros-core

RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

COPY ros_entrypoint.sh /ros_entrypoint.sh

WORKDIR /colcon_ws

COPY slope_estimation src/slope_estimation
COPY slope_estimation_interfaces src/slope_estimation_interfaces

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    colcon build --symlink-install --event-handlers console_direct+ --cmake-args ' -DCMAKE_BUILD_TYPE=Release'

ENV LAUNCH_COMMAND='ros2 run slope_estimation slope_estimator'

# Create build and run aliases
RUN echo 'alias build="colcon build --symlink-install  --event-handlers console_direct+"' >> /etc/bash.bashrc && \
    echo 'alias run="su - ros /run.sh"' >> /etc/bash.bashrc && \
    echo "source /colcon_ws/install/setup.bash; $LAUNCH_COMMAND" >> /run.sh && chmod +x /run.sh
