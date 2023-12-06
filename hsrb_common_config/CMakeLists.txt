# This package has no tests
cmake_minimum_required(VERSION 3.5)
project(hsrb_common_config)

find_package(ament_cmake REQUIRED)

ament_package()

install(DIRECTORY params
  DESTINATION share/${PROJECT_NAME}
  PATTERN ".svn" EXCLUDE
)
