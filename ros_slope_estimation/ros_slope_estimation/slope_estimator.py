# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, MagneticField

class SlopeEstimator(Node):

    def __init__(self):
        super().__init__('slope_estimator')

        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info(f'Initalization finished.')


    def timer_callback(self):

        self.get_logger().info(f'Hello.')


def main(args=None):
    rclpy.init(args=args)

    slope_estimator = SlopeEstimator()

    rclpy.spin(slope_estimator)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    slope_estimator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()