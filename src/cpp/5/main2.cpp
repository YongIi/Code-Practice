#include <iostream>
#include <string>
#include <fstream>
using namespace std;

/*
文件操作-文本文件-写文件

读文件与写文件步骤相似，但读取方式比较多

读文件步骤如下：
1、包含头文件
#include<fstream>
2、创建流对象
ifstream ifs;
3、打开文件并判断文件是否打开成功
ifs.open("文件路径",打开方式)
4、读数据
四种方式读取
5、关闭文件
ifs.close();

*/

// 文本文件 读文件
void test01()
{
    // 1、包含头文件
    // 2、创建流对象
    ifstream ifs;

    // 3、打开文件并判断文件是否打开成功
    ifs.open("test.txt", ios::in);

    // ifs.is_open()文件正常打开时返回true，否则返回false

    if (!ifs.is_open())
    {
        cout << "文件打开失败" << endl;
        return;
    }

    // 4、读数据（忽略空格与回车）
    // 第一种方法
    char buf[1024] = {0};
    while (ifs >> buf)
    {
        cout << buf << endl;
    }

    // 第二种方法
    /*
    char buf[1024] ={0};
    //getline是读取一行，需要两个参数，第一个是读取一行后存入的地址buf，第二个是传入的最大尺寸
    while (ifs.getline(buf,sizeof(buf)))
    {
        cout << buf << endl;
    }
    */

    // 第三种方法
    /*
    string buf;
    while (getline(ifs, buf)) // 使用全局函数getline，第一个参数是输入流对象，第二个参数是读取数据后存入的地址
    {
        cout << buf << endl;
    }
    */

    // 第四种方法（不推荐用）
    /*
    char c;  // 每次只读取一个字符
    while((c=ifs.get())!=EOF)  // 如果没有读到文件尾，则会一直读取。EOF：end of file
    {
        cout << c;
    }
    */

    // 5、关闭文件
    ifs.close();
}

int main()
{
    test01();
    return 0;
}