#include <iostream>
using namespace std;

class Person
{
public:
    Person()
    {
        cout << "调用构造函数" << endl;
    }
    ~Person()
    {
        cout << "调用析构函数" << endl;
    }
};

void test01()
{
    Person p;
}

int main()
{
    test01();
    return 0;
}