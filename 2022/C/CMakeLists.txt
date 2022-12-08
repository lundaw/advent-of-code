cmake_minimum_required (VERSION 3.25)
project (aoc-2022-lundaw-c)
set (C_STANDARD 17)
set (C_STANDARD_REQUIRED On)

add_subdirectory (src)
file (COPY ../../_inputs/2022/ DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/inputs)