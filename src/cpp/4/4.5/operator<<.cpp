#include <iostream>
#include <string>
using namespace std;

//左移运算符重载
class Person
{
    friend ostream &operator<<(ostream &cout, Person &p);
    friend void test01();

public:
    // 利用成员函数重载左移运算符
    // 不能利用成员函数重载<<运算符，因为无法实现cout在左侧
    // void operator<<(cout); 只能把 p.operator<<(cout) 简化为p << cout，这样成员函数重载时，只能是p在左侧
private:
    int m_A;
    int m_B;
};

//只能利用全局函数重载左移运算符
// cout是标准的输出流对象，内置类型是ostream，且cout全局只能有一个，必须用引用的方式进行传递，即该函数内的cout与别处的cout是别名关系（原因：iostram类的对象是不允许复制的，只能引用）
ostream &operator<<(ostream &cout, Person &p) //本质operator<<(cout, p)可以简化为cout << p   因为是别名，在该函数内cout名称可以是out等其他名称，但函数传参时是一定得是cout
{
    cout << "m_A = " << p.m_A << endl;
    cout << "m_B = " << p.m_B << endl;
    return cout; //为了实现链式编程，函数返回cout，且函数的返回值类型为ostream &，保留&同样是因为iostram类的对象是不允许复制的，只能引用
}

void test01()
{
    Person p;
    p.m_A = 10;
    p.m_B = 20;

    cout << p.m_A << endl;
    cout << p.m_B << endl;

    cout << p << "Hello World!" << endl; //实现链式编程思想
}

int main()
{
    test01();
    return 0;
}