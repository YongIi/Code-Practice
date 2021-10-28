#include <iostream>
using namespace std;

class Person
{
public:
    Person()
    {
        cout << "调用默认无参构造函数" << endl;
    }

    Person(int age)
    {
        m_Age = age;
        cout << "调用有参构造函数" << endl;
    }

    Person(const Person &p)
    {
        m_Age = p.m_Age;
        cout << "调用拷贝构造函数" << endl;
    }
    ~Person()
    {
        cout << "调用默认析构函数" << endl;
    }

    int m_Age;
};

void test01()
{
    Person p1(20);
    Person p2(p1);
    cout << p2.m_Age << endl;
}

void doWork(Person p)
{
}

void test02()
{
    Person p;
    doWork(p);
}

Person doWork2()
{
    Person p1;
    cout << (int *)&p1 << endl;
    return p1;
}

void test03()
{
    Person p = doWork2();
    cout << (int *)&p << endl;
}

int main()
{
    //test01();
    //test02();
    test03();
    return 0;
}
