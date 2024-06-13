import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return(LaunchDescription([
        Node(
                package='laser_filters',
                executable='scan_to_scan_filter_chain',
                output='screen',
                name='angle',
                parameters=[{
                    'lower_angle':-1.57,
                    'upper_angle': 1.57

                }]
            )
    ]))

