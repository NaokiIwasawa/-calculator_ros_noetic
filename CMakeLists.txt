cmake_minimum_required(VERSION 3.0.2)
project(calculator)

find_package(catkin REQUIRED COMPONENTS
  rospy
  random
)

catkin_package(
)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
