#include <iostream>
#include <string>
#include <fstream>

using namespace std;

/*
文件操作-文本文件-写文件

程序运行时产生的数据都是临时数据，程序一旦运行结束都会被释放回收
通过文件可以将数据持久化

C++对文件的操作也是基于面向对象的技术，提供一个文件流管理的一个类
C++对文件的操作需要包含头文件<fstream>

文件类型分为两种：
1、文本文件-以ASCII码存在计算机中
2、二进制文件-以二进制形式存储在计算机中，用户一般不能直接读懂它们

操作文件的三大类：
1、ofstream：写操作
2、ifstream：读操作
3、fstream：读写操作

*/

// 文本文件-写文件

/*
写文件步骤如下：
1、包含头文件
#include<fstream>
2、创建流对象
ofstream ofs；
3、打开文件
ofs.open("文件路径", 打开方式)
4、写数据
ofs<<"写入数据";
5、关闭文件
ofs.close();

文件打开方式：
ios::in     为读文件而打开文件
ios::out    为写文件而打开文件
ios::ate    初始位置：文件尾
ios::app    追加方式写文件
ios::trunc  如果文件存在先删除，再创建新的
ios::binary 二进制方式

注意：
文件打开方式可以混合搭配使用，利用|操作符
例如：用二进制方式写文件    ios::binary | ios::out
*/

void test01()
{
    ofstream ofs;
    ofs.open("test.txt", ios::out);
    ofs << "姓名：张三" << endl;
    ofs << "性别：男" << endl;
    ofs << "年龄：18" << endl;
    ofs.close();
}

int main()
{
    test01();
    return 0;
}