cmake_minimum_required(VERSION 2.8.3)
project(tmc_hsrb_description)

find_package(catkin REQUIRED COMPONENTS urdf)

# for beetle
set(HSR_BEETLE_URDF_DIR ${PROJECT_SOURCE_DIR}/urdf/beetle)
set(HSR_BEETLE_URDF ${PROJECT_SOURCE_DIR}/robots/beetle/beetle.urdf)
set(HSR_BEETLE_XACRO ${PROJECT_SOURCE_DIR}/robots/beetle/beetle.urdf.xacro)

add_custom_command(
  OUTPUT ${HSR_BEETLE_URDF}
  DEPENDS ${HSR_BEETLE_URDF_DIR}/*
  COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro.py ${HSR_BEETLE_XACRO} > ${HSR_BEETLE_URDF})

add_custom_target(hsr_urdfs ALL DEPENDS ${HSR_BEETLE_URDF})

catkin_package(
    DEPENDS
    CATKIN_DEPENDS urdf
    INCLUDE_DIRS
    LIBRARIES
    CFG_EXTRAS
)

include_directories(${catkin_INCLUDE_DIRS})

install(DIRECTORY meshes/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes
        PATTERN ".svn" EXCLUDE
)
install(DIRECTORY robots/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/robots
        PATTERN ".svn" EXCLUDE
)

install(DIRECTORY urdf/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
        PATTERN ".svn" EXCLUDE
)
