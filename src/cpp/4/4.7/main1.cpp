#include <iostream>
#include <string>
using namespace std;

/*
多态（多种状态）的基本语法

1、静态多态
包括：函数重载（复用函数名）、运算符重载（复用运算符）
特点：静态多态的函数地址早绑定，编译阶段确定函数地址

2、动态多态
包括：派生类和虚函数
功能：实现运行时多态
特点：动态多态的函数地址晚绑定，运行阶段确定函数地址

# 动态多态的满足条件
1、有继承关系
2、子类要重写父类的虚函数（不是重载，重写是返回值、函数名和参数都要完全一致）（子类函数前面的virtual是可写可不写的）

# 动态多态的使用
3、父类的指针或引用指向（接收）子类对象
4、该指针/引用去调用该虚函数


*/

/*
C++中允许父子之间的类型转换，不需要做强制类型转换，父类的指针或引用可以直接指向子类的对象
即：父类的引用/指针可以接收子类的对象
例如：Animal是父类，Cat是其子类，cat是Cat的对象，则可以有：
Animal &animal = cat；
*/

class Animal
{
public:
    // 虚函数
    virtual void speak()
    {
        cout << "动物在说话" << endl;
    }
};

class Cat : public Animal
{
public:
    // 子类重写父类的虚函数，函数的返回值类型、函数名、参数列表要完全相同
    void speak()
    {
        cout << "小猫在说话" << endl;
    }
};

class Dog : public Animal
{
public:
    // 子类重写父类的虚函数，函数的返回值类型、函数名、参数列表要完全相同
    void speak()
    {
        cout << "小狗在说话" << endl;
    }
};

// 执行说话的函数
// 地址早绑定，在编译阶段确定函数地址，不管传入什么样的动物，都是走Animal中的speak函数
void doSpeak(Animal &animal) // Animal &animal = cat;  // 父类的指针或引用指向（接收）子类对象
{
    animal.speak();
}

// 如果想执行让猫说话，那么这个函数的地址就不能提前绑定，需要在运行阶段进行绑定，地址晚绑定

void test01()
{
    Cat cat;
    doSpeak(cat); // 父类的引用在接收子类的对象

    Dog dog;
    doSpeak(dog);

    Animal animal;
    doSpeak(animal);
}

int main()
{
    test01();
    return 0;
}