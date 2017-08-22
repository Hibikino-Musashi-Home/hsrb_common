# Copyright (C) 2016 Toyota Motor Corporation
# vim: fileencoding=utf-8 :
cmake_minimum_required(VERSION 2.8.3)
project(hsrb_description)

find_package(catkin REQUIRED COMPONENTS xacro rosbash)

# define robots to be installed
# set(robots hsrb4s)
set(robots hsrb1s hsrb2s hsrb3s hsrb4s)

# Gather dae files to be installed
set(_mesh_fiels "")
foreach(_robot ${robots})
    set(_xacro ${PROJECT_SOURCE_DIR}/robots/${_robot}.urdf.xacro)
    # find dae files in expanded urdf
    execute_process(COMMAND bash "-c" "${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} | grep dae | sed -E 's/.*hsrb_description\\/(.*)\"\\/>/\\1/g'" OUTPUT_VARIABLE _dae_files)
    string(REGEX REPLACE "\n" ";" _dae_files "${_dae_files}")
    list(APPEND _mesh_files ${_dae_files})
endforeach()

# remove duplicates
list(REMOVE_DUPLICATES _mesh_files)

catkin_package(CATKIN_DEPENDS xacro)

install(DIRECTORY config launch robots urdf
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
)

foreach(_file ${_mesh_files})
    get_filename_component(_dir ${_file} DIRECTORY)
    install(FILES ${_file} DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${_dir}/)
endforeach()

# make a symbolic link
add_custom_target(link_target ALL
     COMMAND ${CMAKE_COMMAND} -E create_symlink hsrb4s.urdf.xacro ${PROJECT_SOURCE_DIR}/robots/hsrb.urdf.xacro
)

if(CATKIN_ENABLE_TESTING)
    catkin_add_nosetests(test)
endif()
