# Copyright (C) 2017 Toyota Motor Corporation
# vim: fileencoding=utf-8 :
# This package has no tests

cmake_minimum_required(VERSION 2.8.3)
project(hsrb_parts_description)

find_package(catkin REQUIRED COMPONENTS xacro rosbash)

catkin_package(CATKIN_DEPENDS xacro)

install(DIRECTORY urdf meshes
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
)
