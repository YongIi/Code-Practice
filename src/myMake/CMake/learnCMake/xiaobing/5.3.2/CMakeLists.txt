# Set the minimum version of CMake that can be used
cmake_minimum_required(VERSION 3.0)

#project name
project(SWAP)

#add compile options
add_compile_options(-Wall --std=c++11)

#set CMAKE_BUILD_TYPE
set( CMAKE_BUILD_TYPE Debug )

# set output binary path
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

############################################################
# Create a library
############################################################
add_library( swap_lib STATIC src/swap.cpp )

#提供静态库的头文件路径，防止不同目录相同名称的头文件会产生影响，单独用target_include_directories为target添加头文件
target_include_directories( swap_lib PUBLIC ${PROJECT_SOURCE_DIR}/include ) 

############################################################
# Create an executable
############################################################

# Add an executable with the above sources
add_executable( swap_01 main.cpp )

# link the new swap_01 target with the swap_lib target
target_link_libraries( swap_01 swap_lib )