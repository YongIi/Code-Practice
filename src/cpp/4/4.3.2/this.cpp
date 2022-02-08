#include <iostream>
using namespace std;

//1、解决名称冲突
class Person
{
public:
    Person(int age)
    {
        //解决名称冲突，鼠标单击可以显示同一个变量
        this->age = age; //this指针指向被调用的成员函数所属的对象，指向调用成员函数的对象本身
    }

    Person & PersonAddAge(Person &p)    //引用指向本身内存，不用引用就是拷贝了，是以值传递的方式拷贝给一个新创建的对象，不加引用的话返回的就不是对象本身了，而是别的Person对象
    {
        this->age += p.age;
        return *this;   //this指针指向调用成员函数的对象，*this是这个对象的本体
    }

    int age;
};

void test01()
{
    Person p1(18);
    cout << "p1的年龄：" << p1.age << endl;
}

//2、返回对象本身用*this
void test02()
{
    Person p1(10);
    Person p2(10);
    //链式编程思想，可以无限地往后面追加
    p2.PersonAddAge(p1).PersonAddAge(p1).PersonAddAge(p1).PersonAddAge(p1);
    cout << "p2的年龄为 " << p2.age << endl;    //多次<<也用了链式编程思想
}

int main()
{
    test01();
    test02();
    return 0;
}
