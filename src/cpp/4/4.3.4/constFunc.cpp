#include <iostream>
using namespace std;

//常函数
class Person
{
public:
    void showPerson() const
    {
        //隐含在每个成员函数里面都有一个this指针
        //this指针的本质是指针常量，指针的指向（地址）是不可以修改的，若this指向了p则会一直指向p，例如 this=NULL; 是错误的
        //类名 *const this；
        //指针常量指向的值（该地址内的值）是可以修改的，即*this是可以修改的，this->m_A也是可以修改的
        //若想让指针常量指向的值也不允许改动，则添加一个const，也即使用 const 类名 * const this；因为this指针在成员函数是默认隐藏定义的，所以设定该const加在成员函数后面
        //在成员函数后面加const的本质，是修饰this指针，让指针指向的值也不可以修改

        //this->m_A = 100;
        //this = NULL;  //this指针的本质是指针常量，指针的指向（地址）是不可以修改的
        this->m_B;
    }

    void func() {}

    int m_A;
    mutable int m_B; //加关键字mutable：特殊变量，即使在常函数中，也可以修改这个值
};

void test01()
{
    Person p;
    p.showPerson();
}

void test02()
{
    const Person p2; //g++编译器需要给const Person写默认构造函数
    //p2.m_A = 100;
    p2.m_B = 100;

    //常对象只能调用常函数：因为普通的成员函数是允许修改成员变量的，调用普通成员函数会侧面修改成员变量，而常对象不允许修改成员变量，故常对象只能调用常函数
    p2.showPerson();
    //p2.func();
}

int main()
{
    test01();
    return 0;
}