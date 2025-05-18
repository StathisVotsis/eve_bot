import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='sound_firmware',
            executable='sound_alert.py',
            output='screen',
            arguments=[]),
    ])