#include <iostream>
#include <string>
using namespace std;

//继承中的同名静态成员处理方式
class Base
{
public:
    static void func()
    {
        cout << "Base - static void func()的调用" << endl;
    }

    static void func(int a)
    {
        cout << "Base - static void func(int a)的调用" << endl;
    }
    static int m_A;
};

int Base::m_A = 100;

class Son : public Base
{
public:
    static void func()
    {
        cout << "Son - static void func()的调用" << endl;
    }

    static int m_A;
};

int Son::m_A = 200;

//同名静态成员属性
void test01()
{
    Son s;
    // 1，通过对象访问
    cout << "通过对象访问：" << endl;
    cout << "Son  下 m_A = " << s.m_A << endl;
    cout << "Base 下 m_A = " << s.Base::m_A << endl;

    // 1，通过类名访问
    cout << "通过类名访问：" << endl;
    cout << "Son  下 m_A = " << Son::m_A << endl;
    //第一个::代表通过类名方式访问，第二个::代表访问父类作用域下的m_A
    cout << "Base 下 m_A = " << Son::Base::m_A << endl; //通过子类对象访问到父类对象中的m_A，并且是通过类名的方式访问
    cout << "Base 下 m_A = " << Base::m_A << endl;      //直接通过父类的作用域访问m_A
}

//同名静态成员函数
void test02()
{
    Son s;
    // 1，通过对象访问
    cout << "通过对象访问：" << endl;
    s.func();
    s.Base::func();
    // 1，通过类名访问
    cout << "通过类名访问：" << endl;
    Son::func();
    Son::Base::func();
    //同理，子类中若存在同名的静态成员函数，会屏蔽父类中所有的同名成员函数，包括重载的同名函数，以下语句会报错
    // Son::func(100);
    // 如果想访问父类中被隐藏的同名成员，需要加作用域
    Son::Base::func(100);
}

int main()
{
    test01();
    test02();
    return 0;
}