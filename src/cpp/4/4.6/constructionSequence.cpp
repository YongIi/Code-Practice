#include <iostream>
#include <string>
using namespace std;

//继承中的构造和析构顺序
class Base
{
public:
    Base()
    {
        cout << "Base的构造函数!" << endl;
    }

    ~Base()
    {
        cout << "Base的析构函数" << endl;
    }
};

class Son : public Base
{
public:
    Son()
    {
        cout << "Son的构造函数!" << endl;
    }

    ~Son()
    {
        cout << "Son的析构函数" << endl;
    }
};

void test01()
{
    //继承中的构造和析构顺序如下：
    //先构造父类再构造子类，析构的顺序与构造的顺序相反，先析构子类再析构父类
    Son son;
}

int main()
{
    test01();
    return 0;
}