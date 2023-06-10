#include <iostream>
#include <string>
using namespace std;

/*
多态案例——计算器类

C++开发提倡利用多态涉及程序架构

分别利用普通写法和多态技术实现计算器

多态的优点：
1、代码组织结构清晰
2、可读性强
3、利于前期和后期的扩展和维护

在普通实现中，如果想扩展新的功能，需要修改源码
但在真实开发中，提倡“开闭原则”：多扩展进行开放，对修改进行关闭

*/

// 普通实现
class Calculator
{
public:
    int getResult(string oper)
    {
        if (oper == "+")
        {
            return m_Num1 + m_Num2;
        }
        else if (oper == "-")
        {
            return m_Num1 - m_Num2;
        }
        else if (oper == "*")
        {
            return m_Num1 * m_Num2;
        }
    }

    int m_Num1; // 操作数1
    int m_Num2; // 操作数2
};

void test01()
{
    // 创建计算器对象
    Calculator c;
    c.m_Num1 = 10;
    c.m_Num2 = 2;

    cout << c.m_Num1 << " + " << c.m_Num2 << " = " << c.getResult("+") << endl;
    cout << c.m_Num1 << " - " << c.m_Num2 << " = " << c.getResult("-") << endl;
    cout << c.m_Num1 << " * " << c.m_Num2 << " = " << c.getResult("*") << endl;
}

// 利用多态实现计算器
// 实现计算器抽象类（什么功能都不用写，只是把getResult函数抽象出来）
class AbstractCalculator
{
public:
    virtual int getResult()
    {
        return 0;
    }

    int m_Num1;
    int m_Num2;
};

// 加法计算器类
class AddCalculator : public AbstractCalculator
{
public:
    virtual int getResult() // virtual关键字可以删除
    {
        return m_Num1 + m_Num2;
    }
};

// 减法计算器类
class SubCalculator : public AbstractCalculator
{
public:
    int getResult()
    {
        return m_Num1 + m_Num2;
    }
};

// 乘法计算器类
class MulCalculator : public AbstractCalculator
{
public:
    int getResult()
    {
        return m_Num1 * m_Num2;
    }
};

void test02()
{
    // 多态使用条件
    // 父类的指针/引用指向子类对象

    // 加法运算
    AbstractCalculator *abc = new AddCalculator;

    abc->m_Num1 = 10;
    abc->m_Num2 = 5;
    cout << abc->m_Num1 << " + " << abc->m_Num2 << " = " << abc->getResult() << endl;

    // 用完后记得销毁，释放了堆区的内存，但abc始终是父类的指针
    delete abc;

    // 减法运算
    abc = new SubCalculator;

    abc->m_Num1 = 10;
    abc->m_Num2 = 5;
    cout << abc->m_Num1 << " - " << abc->m_Num2 << " = " << abc->getResult() << endl;
    delete abc;

    // 乘法运算
    abc = new MulCalculator;
    abc->m_Num1 = 10;
    abc->m_Num2 = 5;
    cout << abc->m_Num1 << " * " << abc->m_Num2 << " = " << abc->getResult() << endl;
    delete abc;
}

int main()
{
    test01();
    test02();
    return 0;
}