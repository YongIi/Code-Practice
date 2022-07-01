PROJECT (HELLO) #工程名，工程名和生成的可执行文件hello是没有任务关系的
add_subdirectory(src bin)   #向当前⼯程添加存放源⽂件的⼦⽬录src，并可以指定中间⼆进制和⽬标⼆进制存放的位置，bin文件夹会被自动创建
                            #如果不进⾏ bin ⽬录的指定，那么编译结果(包括中间结果)都将存放在build/bin ⽬录

#注意：一般可以不在以上命令中指定bin的路径，避免浪费内存
#add_subdirectory(src)
#以上命令中的bin路径和SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)指定的bin路径是有区别的，
#前者是在指定中间文件和最终文件的路径，一般是在编译工程的路径下，即build/bin
#后者是指定最终生成的二进制文件的路径，一般是在工程顶层目录，与src,include等文件夹同级别
