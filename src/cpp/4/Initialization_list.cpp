#include <iostream>
using namespace std;

class Person
{
public:
    // 传统初始化操作
    // Person(int a, int b, int c)
    // {
    //     m_A = a;
    //     m_B = b;
    //     m_C = c;
    // }

    //用初始化列表初始化属性
    // Person() : m_A(10), m_B(20), m_C(30)
    // {
    // }

    Person(int a, int b, int c) : m_A(a), m_B(b), m_C(c)
    {
    }

    int m_A;
    int m_B;
    int m_C;
};

void test01()
{
    Person p(10, 20, 30);
    //Person p;
    cout << "m_A = " << p.m_A << endl;
    cout << "m_B = " << p.m_B << endl;
    cout << "m_C = " << p.m_C << endl;
}

int main()
{
    test01();
    return 0;
}