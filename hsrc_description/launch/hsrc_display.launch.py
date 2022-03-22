#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Toyota Motor Corporation
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    hsrb_description_dir = get_package_share_directory('hsrb_description')
    view_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([hsrb_description_dir, '/launch/hsrb_display.launch.py']),
        launch_arguments={'description_package': 'hsrc_description',
                          'description_file': 'hsrc1s.urdf.xacro'}.items())
    return LaunchDescription([view_launch])
