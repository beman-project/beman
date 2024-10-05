cmake_minimum_required(VERSION 3.23)
project(BemanIntegrationTest CXX)
include(CTest)

find_package(example REQUIRED)
find_package(scn REQUIRED)

# We are using the tests from the beman repo as a whole to test
# whether the beman package in Conan was packaged correctly.
add_subdirectory(
  "${CMAKE_CURRENT_SOURCE_DIR}/../../../../../tests"
  # Normally you don't need to specify a second parameter to add_subdirectory,
  # but since the tests are not in this subdirectory, we need to clarify where
  # to place relevant CMake configuration state. This name is arbitrary other
  # than being unlikely to collide with anything else accidentally.
  "beman_tests"
  )
