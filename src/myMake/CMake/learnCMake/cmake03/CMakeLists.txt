PROJECT (HELLO) #工程名，工程名和生成的可执行文件hello是没有任务关系的
add_subdirectory(src bin)   #向当前⼯程添加存放源⽂件的⼦⽬录src，并可以指定中间⼆进制和⽬标⼆进制存放的位置，bin文件夹会被自动创建
                            #如果不进⾏ bin ⽬录的指定，那么编译结果(包括中间结果)都将存放在build/bin ⽬录

#注意：一般可以不在以上命令中指定bin的路径，避免浪费内存
#add_subdirectory(src)
#以上命令中的bin路径和SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)指定的bin路径是有区别的，
#前者是在指定中间文件和最终文件的路径，一般是在编译工程的路径下，即build/bin
#后者是指定最终生成的二进制文件的路径，一般是在工程顶层目录，与src,include等文件夹同级别


#安装文件
#FILES：⽂件
#DESTINATION：
#1、写绝对路径
#2、可以写相对路径，相对路径实际路径是：${CMAKE_INSTALL_PREFIX}/<DESTINATION 定义的路径>
#CMAKE_INSTALL_PREFIX 默认是在 /usr/local/
#cmake -DCMAKE_INSTALL_PREFIX=/usr 可以在cmake的时候指定CMAKE_INSTALL_PREFIX变量的路径
install(FILES COPYRIGHT README DESTINATION /home/cfdmaker/cmakeTestInstall)

#安装脚本
#PROGRAMS：⾮⽬标⽂件的可执⾏程序安装(⽐如脚本之类)
#INSTALL(PROGRAMS runhello.sh DESTINATION bin)是采用的相对路径，会将脚本安装到/usr/local/bin
install(PROGRAMS runhello.sh DESTINATION /home/cfdmaker/cmakeTestInstall/bin)

#安装整个文件夹
INSTALL(DIRECTORY doc DESTINATION /home/cfdmaker/cmakeTestInstall)
#注意：abc 和 abc/有很⼤的区别
#⽬录名不以/结尾：这个⽬录将被安装为⽬标路径下的
#⽬录名以/结尾：将这个⽬录中的内容安装到⽬标路径

#安装可执行文件，该语句要放在子文件夹src下的CMakeLists.txt文件中
#install(TARGETS hello DESTINATION /home/cfdmaker/cmakeTestInstall/bin)