PROJECT (HELLO) #工程名，工程名和生成的可执行文件hello是没有任务关系的
SET(SRC_LIST main.cpp)  #显示地定义变量，SRC_LIST包含后面的文件
MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})   #MESSAGE向终端输出用户自定义的信息，STATUS是输出前缀为--的信息
MESSAGE(STATUS "This is SOURCE dir "${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello ${SRC_LIST})   #生成可执行程序hello，源文件要读取SRC_LIST中的内容

#语法规则
#1，变量使用${}取值，在IF语句中直接使用变量名
#2，指令(参数 1 参数 2...) 参数使⽤括弧括起，参数之间使⽤空格或分号分开，一般用空格
#3，指令是⼤⼩写⽆关的，推荐全部使⽤⼤写指令；参数和变量是⼤⼩写相关的

#注意事项
#1，SET(SRC_LIST main.cpp) 可以写成 SET(SRC_LIST “main.cpp”)，如果源⽂件名中含有空格，就必须要加双引号
#2，ADD_EXECUTABLE(hello main) 后缀可以不写，他会⾃动去找.c和.cpp，最好不要这样写，可能会有这两个⽂件main.cpp和main