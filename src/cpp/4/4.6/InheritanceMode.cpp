#include <iostream>
#include <string>
using namespace std;

//继承方式

class Base1
{
public:
    int m_A;

protected:
    int m_B;

private:
    int m_C;
};

//公共继承
class Son1 : public Base1
{
public:
    void func()
    {
        m_A = 10; //父类中公共权限的成员，到子类依然是公共权限
        m_B = 20; //父类中保护权限的成员，到子类依然是保护权限
        //m_C=30； //父类中的私有权限成员，子类访问不到
    }
};

//保护继承
class Son2 : protected Base1
{
    public:
    void func()
    {
        m_A = 10; //父类中公共权限的成员，到子类变为保护权限
        m_B = 20; //父类中保护权限的成员，到子类依然是保护权限
        //m_C=30； //父类中的私有权限成员，子类访问不到
    }
};

//私有继承
class Son3 : private Base1
{
    public:
    void func()
    {
        m_A=100; //父类中公共权限的成员，到子类变为私有权限
        m_B=200; //父类中保护权限的成员，到子类变为私有 权限
        //m_C=300; //父类中的私有权限成员，子类访问不到
    }
};

void test01()
{
    Son1 s1;
    s1.m_A =100;
    //s1.m_B =200; //到Son1中m_B是保护权限，类外访问不到

    Son2 s2;
    //s2.m_A=1000; //在Son2中，m_A变成了保护权限，因此类外访问不到
    //s2.m_B=2000; //在Son2中的m_B是保护权限，也不能访问

    Son3 s3;
    //s3.m_A=1000; //在Son3中变成了私有成员，类外访问不到
}

int main()
{
    return 0;
}