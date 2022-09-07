#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Toyota Motor Corporation
from launch import LaunchDescription

from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def declare_arguments():
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument('description_package',
                              default_value='hsrb_description',
                              description='Description package with robot URDF/xacro files.'))
    declared_arguments.append(
        DeclareLaunchArgument('description_file',
                              default_value='hsrb4s.urdf.xacro',
                              description='URDF/XACRO description file with the robot.'))
    return declared_arguments


def generate_launch_description():
    description_package = LaunchConfiguration('description_package')
    description_file = LaunchConfiguration('description_file')
    robot_description_content = Command(
        [PathJoinSubstitution([FindExecutable(name='xacro')]), ' ',
         PathJoinSubstitution([FindPackageShare(description_package), 'robots', description_file])])

    robot_description = {'robot_description': robot_description_content}
    rviz_config_file = PathJoinSubstitution([FindPackageShare('hsrb_description'), 'launch', 'display.rviz'])

    joint_state_publisher_node = Node(package='joint_state_publisher_gui',
                                      executable='joint_state_publisher_gui')
    robot_state_publisher_node = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      parameters=[robot_description])
    rviz_node = Node(package='rviz2',
                     executable='rviz2',
                     arguments=['-d', rviz_config_file])

    nodes = [joint_state_publisher_node, robot_state_publisher_node, rviz_node]
    return LaunchDescription(declare_arguments() + nodes)
