# copyright TOYOTA MOTOR CORPORATION
# vim: fileencoding=utf-8 :
cmake_minimum_required(VERSION 2.8.3)
project(tmc_hsrb_description)

find_package(catkin REQUIRED COMPONENTS xacro)

set(HSRB_URDF_DIR ${PROJECT_SOURCE_DIR}/urdf)
set(HSRB_URDF ${PROJECT_SOURCE_DIR}/robots/hsrb.urdf)
set(HSRB_XACRO ${PROJECT_SOURCE_DIR}/robots/hsrb.urdf.xacro)

add_custom_command(
  OUTPUT ${HSRB_URDF}
  DEPENDS ${HSRB_XACRO} ${HSRB_URDF_DIR}/*
  COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro.py ${HSRB_XACRO} > ${HSRB_URDF})

add_custom_target(hsrb_urdf ALL DEPENDS ${HSRB_URDF})

catkin_package(
    DEPENDS
    CATKIN_DEPENDS xacro
    INCLUDE_DIRS
    LIBRARIES
    CFG_EXTRAS
)

install(DIRECTORY launch meshes robots urdf
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
)

if(CATKIN_ENABLE_TESTING)
    catkin_add_nosetests(test)
endif()
