#include <iostream>
using namespace std;

class Person
{
public:
    Person()
    {
        cout << "无参构造函数" << endl;
    }

    Person(int a)
    {
        age = a;
        cout << "有参构造函数" << endl;
    }

    Person(const Person &p)
    {
        age = p.age;
        cout << "拷贝构造函数" << endl;
    }

    ~Person()
    {
        cout << "析构函数" << endl;
    }

public:
    int age;
};

void test01()
{
    Person p;
}

void test02()
{
    Person p1(10);

    Person p2(p1);
}

int main()
{
    test01();
    test02();
    return 0;
}