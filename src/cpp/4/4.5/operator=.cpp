#include <iostream>
#include <string>
using namespace std;

//赋值运算符重载

class Person
{
public:
    Person(int age)
    {
        m_Age = new int(age);
    }
    ~Person()
    {
        if (m_Age != NULL)
        {
            delete m_Age;
            m_Age = NULL;
        }
    }

    //重载赋值运算符，有该重载函数后，编译器不再提供默认的赋值运算
    Person &operator=(Person &p)
    {
        //编译器提供的浅拷贝
        // m_Age = p.m_Age;

        //应该先判断是否有属性在堆区，如果有先释放干净再深拷贝
        if (m_Age != NULL)
        {
            delete m_Age;
            m_Age = NULL;
        }
        m_Age = new int(*p.m_Age);
        //之所以不用以下命令是因为：如果不调用有参构造而是调用的默认的无参构造函数，p2还没来得及给m_Age分配堆区的内存，以下命令也没办法赋值
        //*m_Age = *p.m_Age;

        //返回对象本身
        return *this;
    }

    int *m_Age;
};

void test01()
{
    Person p1(18);
    Person p2(20);
    Person p3(30);
    p3 = p2 = p1;
    cout << "p1的年龄是：" << *p1.m_Age << endl;
    cout << "p2的年龄是：" << *p2.m_Age << endl;
    cout << "p3的年龄是：" << *p3.m_Age << endl;
}

int main()
{
    test01();

    int a = 10;
    int b = 20;
    int c = 30;

    c = b = a; //赋值运算符的运算顺序是从右到左

    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "c = " << c << endl;

    return 0;
}