import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='nano_firmware',
            executable='serial_tx_rx.py',
            output='screen',
            arguments=[]),
    ])