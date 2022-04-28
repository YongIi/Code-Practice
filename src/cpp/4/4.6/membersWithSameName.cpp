#include <iostream>
#include <string>
using namespace std;

//继承中同名成员处理
class Base
{
public:
    Base()
    {
        m_A = 100;
    }

    void func()
    {
        cout << "Base作用域下func()调用" << endl;
    }

    void func(int a)
    {
        cout << "Base作用域下func(int a)调用" << endl;
    }
    int m_A;
};

class Son : public Base
{
public:
    Son()
    {
        m_A = 200;
    }

    void func()
    {
        cout << "Son 作用域下func()调用" << endl;
    }

    int m_A;
};

//同名成员属性的处理
void test01()
{
    Son s;
    cout << "Son  下的m_A = " << s.m_A << endl;
    //如果通过子类对象访问到父类中的同名成员，需要加一个作用域
    cout << "Base 下的m_A = " << s.Base::m_A << endl;
}

//同名成员函数的处理
void test02()
{
    Son s2;
    s2.func();       //直接调用子类中的同名成员
    s2.Base::func(); //同名时，子类对象访问父类的成员需要加作用域。但如果不同名，父类的某个成员，在子类中没有该成员的同名成员，子类对象也可以直接用.来访问

    //如果子类中出现和父类同名的成员函数，子类的同名成员会隐藏掉父类中所有同名成员
    //那么如果父类的同名成员函数发生重载，子类又有同名成员函数，则无法通过.对重载函数直接访问，下面的语句就会报错
    // s2.func(100):
    //如果想访问到父类中被隐藏的同名成员函数，需要加作用域
    s2.Base::func(100);
}

int main()
{
    test01();
    test02();
    return 0;
}