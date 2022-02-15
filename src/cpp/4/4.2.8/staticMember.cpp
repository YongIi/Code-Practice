#include <iostream>
using namespace std;

class Person
{
public:
    //静态成员变量
    //1，所有对象共享同一份数据
    //2，在编译阶段就分配内存到全局区
    //3，类内要声明，类外要初始化
    static int m_A;

    //静态成员变量也是有访问权限的
private:
    static int m_B;
};

int Person::m_A = 100;  //在全局区命名一个int类型的变量命名为m_A，其作用域是Person
int Person::m_B = 1000; //该数据因为private权限问题在类外是访问不到的

void test01()
{
    Person p;
    cout << p.m_A << endl;
    Person p2;
    p2.m_A = 200;
    cout << p.m_A << endl;
}

void test02()
{
    /*
    静态成员变量不属于某一个对象，所有对象都共享同一份数据
    因此静态成员变量有两种访问方式
    1、通过对象进行访问
    2、通过类名进行访问
    */

    //1、通过对象进行访问
    Person p3;
    cout << p3.m_A << endl;
    //2、通过类名进行访问
    cout << Person::m_A << endl;
    //cout << Person::m_B << endl;  //类外访问不到私有静态成员变量
}

int main()
{
    test01();
    test02();
    return 0;
}