# Copyright (C) 2017 Toyota Motor Corporation
# vim: fileencoding=utf-8 :
# This package has no tests

cmake_minimum_required(VERSION 3.5)
project(hsrb_parts_description)

find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)

install(
  DIRECTORY urdf meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.dsv.in")

ament_package()
