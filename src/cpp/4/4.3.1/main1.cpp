#include <iostream>
using namespace std;

//成员变量与成员函数分开存储
class Person
{
    int m_A;    //非静态成员变量，属于类的对象上
    static int m_B; //静态成员变量，不属于类的对象上
    void func() {}  //非静态成员函数，不属于类的对象上
    static void func2() {}  //静态成员函数，不属于类的对象上
};

int Person::m_B = 0;

void test01()
{
    Person p; //查看对象到底占用多少内存空间
    //空对象占用的内存空间为1个字节
    //c++编译器会给每个空对象也分配一个字节的空间，以区分不同空对象所占内存的位置
    //每个空对象都有一个独一无二的内存地址
    cout << "size of p = " << sizeof(p) << endl;
}

void test02()
{
    Person p;
    cout << "size of p = " << sizeof(p) << endl;
}

int main()
{
    //test01();
    test02();
    return 0;
}