import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='ina260',
            executable='ina260.py',
            output='screen',
            arguments=[]),
    ])