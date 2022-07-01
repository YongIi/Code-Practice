include_directories(/home/cfdmaker/cmakeTestInstall/include/hello) #编译时指定第三方库的头文件路径，还可以将头文件的路径给到环境变量CMAKE_INCLUDE_PATH

#该命令一定要放在下一条命令add_executable的前面
LINK_DIRECTORIES(/home/cfdmaker/cmakeTestInstall/lib) #还可以将共享库的路径给到环境变量CMAKE_LIBRARY_PATH，官方不建议使用该命令，取而代之的为find_package()  find_library()

add_executable(hello main.cpp)

TARGET_LINK_LIBRARIES(hello libhello.so)    #该命令一定要放在上一条命令add_executable的后面

#对于第三方的库文件
#在编译时：
#需要用include_directories指定第三方库的头文件路径，或者将头文件的路径给到环境变量CMAKE_INCLUDE_PATH
#需要用LINK_DIRECTORIES添加⾮标准的共享库搜索路径，或者将共享库的路径给到环境变量CMAKE_LIBRARY_PATH
#需要用TARGET_LINK_LIBRARIES添加需要链接的共享库
#在运行时：
#如果在运行时找不到相应的动态库，需要将动态库的绝对路劲添加到该环境变量中：
#export LD_LIBRARY_PATH =  /usr/include/xxxx:$LD_LIBRARY_PATH
#别忘了添加后要source ~/.bashrc

