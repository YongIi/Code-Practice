#include <iostream>
#include <string>
using namespace std;

//函数调用运算符重载——重载小括号

//打印输出类
class MyPrint
{
    //通过一个对象，直接用小括号()像函数一样调用
public:
    //重载函数调用运算符
    void operator()(string test)
    {
        cout << test << endl;
    }

    void operator()()
    {
        cout << "仿函数可以不要参数，但重载()时有两个括号" << endl;
    }
};

void MyPrint02(string test)
{
    cout << test << endl;
}

void test01()
{
    MyPrint myPrint;
    myPrint("Hello World!"); //由于使用起来非常像函数调用，因此称为仿函数——重载小括号
    myPrint();
    MyPrint02("Hello World!");
}

//仿函数非常灵活，没有固定写法
//加法类
class MyAdd
{
public:
    int operator()(int num1, int num2)
    {
        return num1 + num2;
    }
};

void test02()
{
    MyAdd myAdd;
    int ret = myAdd(1, 2); //先创建对象，再调用仿函数
    cout << "ret = " << ret << endl;

    //匿名函数对象 通过类名+()可以创建一个匿名对象，例如MyAdd()，匿名对象的特点：当前行执行完后立即释放。同时匿名对象调用仿函数，称为匿名函数对象。
    cout << MyAdd()(2, 3) << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}