SET(LIBHELLO_SRC hello.cpp)
#ADD_LIBRARY(hello SHARED ${LIBHELLO_SRC})

#SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib) #指定输出路径

## 同时构建动态库和静态库
#如果⽤这种⽅式，只会构建⼀个动态库，不会构建出静态库，虽然静态库的后缀是.a，因为两者target不能重名
#ADD_LIBRARY(hello SHARED ${LIBHELLO_SRC})
#ADD_LIBRARY(hello STATIC ${LIBHELLO_SRC})
#修改静态库的名字，这样是可以的，但是我们往往希望他们的名字是相同的，只是后缀不同⽽已
#ADD_LIBRARY(hello SHARED ${LIBHELLO_SRC})
#ADD_LIBRARY(hello_static STATIC ${LIBHELLO_SRC})

ADD_LIBRARY(hello_static STATIC ${LIBHELLO_SRC}) #因为hello作为一个target是不能重名的，与下面的动态库不能重名，故用hello_static，但可以用下面的命令参数修改名称
#对hello_static的重名为hello
SET_TARGET_PROPERTIES(hello_static PROPERTIES OUTPUT_NAME "hello")
#cmake 在构建⼀个新的target 时，会尝试清理掉其他使⽤这个名字的库，例如在构建 libhello.so 时， 就会清理掉 libhello.a，为了避免这个问题，采用下面的命令
SET_TARGET_PROPERTIES(hello_static PROPERTIES CLEAN_DIRECT_OUTPUT 1)

ADD_LIBRARY(hello SHARED ${LIBHELLO_SRC})
SET_TARGET_PROPERTIES(hello PROPERTIES OUTPUT_NAME "hello")
SET_TARGET_PROPERTIES(hello PROPERTIES CLEAN_DIRECT_OUTPUT 1)

#安装头文件
#我们需要将libhello.a, libhello.so.x以及hello.h安装到系统目录，才能真正让其他人开发使用
INSTALL(FILES hello.h DESTINATION /home/cfdmaker/cmakeTestInstall/include/hello)   
#我不是不想安装进/usr/local所以用的绝对路径，一般是用相对路径配合prefix来指定安装路径
#cmake -DCMAKE_INSTALL_PREFIX=/usr .. 
#-DCMAKE_INSTALL_PREFIX用来在cmake配置的时候指定安装路径，两点..表示采用上一级目录的CMakeLists.txt文件

#安装库文件
#⼆进制，静态库，动态库安装都⽤TARGETS
#ARCHIVE 特指静态库，LIBRARY 特指动态库，RUNTIME 特指可执⾏⽬标⼆进制。故下面的LIBRARY DESTINATION是动态库安装路径，ARCHIVE DESTINATION是静态库安装路径
INSTALL(TARGETS hello hello_static LIBRARY DESTINATION /home/cfdmaker/cmakeTestInstall/lib ARCHIVE DESTINATION /home/cfdmaker/cmakeTestInstall/lib)