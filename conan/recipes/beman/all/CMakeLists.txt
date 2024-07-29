cmake_minimum_required(VERSION 3.15)
project(beman NONE)
include(CTest)

if(ENABLE_TESTING)
  add_subdirectory("${CMAKE_CURRENT_LIST_DIR}/../../tests")
endif()
