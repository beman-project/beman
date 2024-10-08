# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

add_executable(beman_example beman_example.cpp)
target_link_libraries(beman_example PRIVATE example::example scn::scn)
