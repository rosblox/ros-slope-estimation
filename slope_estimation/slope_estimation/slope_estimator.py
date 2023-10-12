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

import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, MagneticField

from slope_estimation_interfaces.srv import GetFloat32


class SlopeEstimator(Node):

    def __init__(self):
        super().__init__('slope_estimator')
        self.create_subscription(Imu, '/imu/data_raw', self.imu_callback, 3)
        self.slope_estimation_srv = self.create_service(GetFloat32, '~/get_slope_estimate', self.service_callback)

    def service_callback(self, request, response):
        response.data = self.slope
        return response

    def imu_callback(self, msg):
        acc_x = msg.linear_acceleration.x
        acc_y = msg.linear_acceleration.y
        acc_z = msg.linear_acceleration.z

        self.slope = math.atan2(math.sqrt(acc_x*acc_x+acc_y*acc_y), acc_z)  


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
