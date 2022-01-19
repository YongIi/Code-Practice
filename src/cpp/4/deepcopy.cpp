#include <iostream>
using namespace std;

class Person
{
public:
    Person()
    {
        cout << "Person的默认构造函数调用" << endl;
    }
    Person(int age, int height)
    {
        m_Age = age;
        m_Height = new int(height); //为什么开辟到堆区：因为堆区的数据可以手动释放，在函数体外也可以使用。在实际应用中，用到堆区而且又需要拷贝的时候要防止指针悬挂的问题
        cout << "Person的有参构造函数调用" << endl;
    }
    //自己写一个深拷贝解决浅拷贝带来的问题：问题1：两个对象指向堆区同一个内存，不能各指各的；问题2：释放对象时会造成非法操作——同一个堆区内存被重复释放
    Person(const Person &p)
    {
        cout << "Person深拷贝构造函数的调研" << endl;
        //编译器写的默认浅拷贝如下：
        //m_Age = p.m_Age;
        //m_Height = p.m_Height;

        //自己写的深拷贝如下：
        m_Age = p.m_Age;
        m_Height = new int(*p.m_Height);
    }

    ~Person()
    {
        //析构代码需要把在堆区开辟的数据释放干净，否则下面的test01函数结束后会把对象p1和p2的数据释放，但堆区开辟的数据则会一直保留，占据内存(内存泄漏)
        if (m_Height != NULL)
        {
            delete m_Height; //释放堆区内存
            m_Height = NULL; //防止野指针的出现，进行置空的操作。指针不知道该指向何处时，指向NULL
        }
        cout << "Person的析构函数调用" << endl;
    }

    int m_Age;
    int *m_Height; //为什么用指针来指向身高，因为要把身高的数据开辟到堆区
};

void test01()
{
    Person p1(10, 160);
    cout << "p1的年龄为: " << p1.m_Age << " 身高为： " << *p1.m_Height << endl;

    Person p2(p1);
    cout << "p2的年龄为: " << p2.m_Age << " 身高为： " << *p2.m_Height << endl;

    *p2.m_Height = 180;
    cout << "修改的身高为： " << *p2.m_Height << endl;
}

int main()
{
    test01();
    return 0;
}