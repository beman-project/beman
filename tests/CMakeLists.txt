
add_executable(beman_example beman_example.cpp)
target_link_libraries(beman_example PRIVATE example::example scn::scn)
add_test(NAME beman_example COMMAND beman_example)
