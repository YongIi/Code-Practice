#include <iostream>
using namespace std;

//静态成员函数
//所有对象共享同一个函数
//静态成员函数只能访问静态成员变量

class Person
{
public:
    static void func()
    {
        m_A = 200;
        //m_B = 200;    //静态成员函数不可以访问非静态成员变量，因为静态函数作为共享函数，不知道该修改哪一个对象的m_B
        cout << "static void func的调用" << endl;
    }

    static int m_A; //类内要声明，类外要初始化
    int m_B;

    //静态成员函数也是有访问权限的，private权限的函数在类外访问不到
    private:
    static void func2()
    {
        cout << "static void func2的调用" << endl;
    }
};

int Person::m_A = 100;

void test01()
{
    //1、通过对象进行访问
    Person p;
    p.func();
    //2、通过类名进行访问
    Person::func();
    //Person::func2();  //类外不能调用私有的静态成员函数
}

int main()
{
    test01();
    return 0;
}