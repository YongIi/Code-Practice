add_executable(hello main.cpp)

#以下指定路径的命令要放在子文件夹内的CMakeLists.txt中
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin) #将生成的可执行文件放至指定的路径，PROJECT_SOURCE_DIR是工程顶层目录，PROJECT_BINARY_DIR是工程编译发生的目录，即build目录
SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)