#include <iostream>
#include <string>
using namespace std;

//重载递增运算符

//自定义整型
class myInteger
{
    friend ostream &operator<<(ostream &cout, myInteger myint);

public:
    myInteger()
    {
        m_Num = 0;
    }

    //重载前置++运算符
    myInteger &operator++() //链式编程必须引用，不然返回本对象时会创造新的同类对象进行接收。返回引用是为了一直对一个数据进行递增
    {
        //先进行++运算
        ++m_Num;
        //再将自身做返回
        return *this;
    }
    //前置递增返回引用，后置递增返回值

    //重载后置++运算符
    //后置递增函数类型一定不能返回&，因为局部的临时对象temp会在当前函数执行完后被释放掉，即使该地址被引用为别名，下一个语句也不能访问到正确的数据（已被释放），再访问属于非法操作，所以只能创建一个新的对象传递数据
    //此外，后置++无法进行链式编程，就连编译器默认的(a++)++都会编译报错，所以除非必须，否则不用递增递减的后置版本
    myInteger operator++(int) // int代表占位参数，可以用于区分前置和后置递增
    {
        //先记录当时的结果
        myInteger temp = *this;
        //后++递增
        m_Num++;
        //最后将当时记录的结果做返回
        return temp;
    }

private:
    int m_Num;
};

//重载左移<<运算符
ostream &operator<<(ostream &cout, myInteger myint) //同理，因为后置++运算符传过来的是一个新建的临时对象，其接收也不能用引用的方式，因为临时对象的数据会在传完后被释放，不能被引用，故第二个参数的类型不能加&
{
    cout << myint.m_Num;
    return cout;
}

void test01()
{
    myInteger myint;

    cout << myint << endl;
    cout << ++(++myint) << endl;
    cout << myint << endl;
}

void test02()
{
    myInteger myint;
    cout << myint << endl;
    cout << myint++ << endl;
    // cout << (myint++)++ << endl;  //不合适的语句，即使语法允许这样写，但执行时会创建临时对象递增一次，且没应用到myint上
    cout << myint << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}