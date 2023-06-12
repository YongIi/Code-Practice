#include <iostream>
#include <string>
#include <fstream>
using namespace std;

/*
二进制文件——读文件

二进制方式读取文件主要利用流对象调用成员函数read
函数原型：
istream& read(char * buffer, int len);
参数解释：
字符指针buffer指向内存中一段存储空间，它指定要把数据读到哪，是读出来传给的地址。len是读写的（最大）字节数
eg:
ifs.read((char *)&p, sizeof(Person)); // 使用(char *)强制转化类型是因为参数要求它传入这样的类型
*/

class Person
{
public:
    char m_Name[64];
    int m_Age;
};

void test01()
{
    // 1、包含头文件
    // 2、创建流对象
    ifstream ifs;

    // 3、打开文件并判断文件是否打开成功
    ifs.open("person.txt", ios::in | ios::binary);

    if (!ifs.is_open()) // 判断文件路径是否有错，是否能正确打开文件
    {
        cout << "文件打开失败" << endl;
        return;
    }

    // 4、读文件
    Person p;

    ifs.read((char *)&p, sizeof(Person)); // 使用(char *)强制转化类型是因为参数要求它传入这样的类型

    cout << "姓名：" << p.m_Name << " 年龄：" << p.m_Age << endl;

    // 5、关闭文件
    ifs.close();
}

int main()
{
    test01();
    return 0;
}