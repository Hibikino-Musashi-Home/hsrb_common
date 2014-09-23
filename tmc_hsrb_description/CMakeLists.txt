cmake_minimum_required(VERSION 2.8.3)
project(tmc_hsrb_description)

find_package(catkin REQUIRED COMPONENTS urdf)

# for beetle
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
    CATKIN_DEPENDS urdf
    INCLUDE_DIRS
    LIBRARIES
    CFG_EXTRAS
)

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
