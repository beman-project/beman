
cmake_minimum_required(VERSION 3.23)
project(beman LANGUAGES CXX)

include(CTest)

include(FetchContent)
FetchContent_Declare(
  example
  GIT_REPOSITORY https://github.com/beman-org/example.git
  GIT_TAG        main
)

FetchContent_Declare(
  scn
  GIT_REPOSITORY https://github.com/eliaskosunen/scnlib
  GIT_TAG        v2.0.2
)

FetchContent_MakeAvailable(
  example
  scn
)

add_subdirectory(example)
