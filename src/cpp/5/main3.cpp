#include <iostream>
#include <string>
#include <fstream>
using namespace std;

/*
二进制文件——写文件

以二进制的方式对文件进行读写操作

打开方式要指定为ios::binary

二进制方式写文件主要利用流对象调用成员函数write
函数原型：
ostream& write(const char * buffer, int len);
参数解释：
字符指针buffer指向内存中一段存储空间，它是要写出的数据的地址；len是读写的字节数，即写出的长度
eg:
ofs.write((const char *)&p, sizeof(Person)); // 使用(const char *)强制转化类型是因为参数要求它传入的类型

写的数据类型可以是自定义的数据类型

注意，在二进制文件中写字符串的时候，最好不要用string类型，而是用字符char c[]数组
*/

class Person // 不写构造函数时，它有默认的构造函数
{
public:
    char m_Name[64]; // 注意，在二进制文件中写字符串的时候，最好不要用string类型，而是用字符char c[]数组
    int age;
};

void test01()
{
    // 1、包含头文件fstream
    // 2、创建流对象
    ofstream ofs;

    // 3、打开文件
    ofs.open("person.txt", ios::out | ios::binary);
    // ofstream ofs("person.txt", ios::out | ios::binary);  // 使用构造函数，两步合成一步

    // 4、写文件
    Person p = {"张三", 18};
    ofs.write((const char *)&p, sizeof(Person)); // 使用(const char *)强制转化类型是因为参数要求它传入这样的类型

    // 5、关闭文件
    ofs.close();

    cout << p.m_Name << " " << p.age << endl; // 检查默认构造函数是否生效
}

int main()
{
    test01();
    return 0;
}