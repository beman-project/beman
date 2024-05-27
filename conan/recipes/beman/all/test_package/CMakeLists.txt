cmake_minimum_required(VERSION 3.23)
project(BemanIntegrationTest CXX)

find_package(example REQUIRED)
find_package(scn REQUIRED)

add_executable(beman-integration-test)
target_sources(beman-integration-test PRIVATE
  src/beman/integration_test.cpp
)
target_link_libraries(beman-integration-test PRIVATE
  example::example
  scn::scn
)
