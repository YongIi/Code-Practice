#include <iostream>
#include <string>
using namespace std;

/*
多态的原理剖析

当父类中对成员函数添加virtual后，父类的内部结构发生了改变，类中多了一个虚函数(表)指针vfptr

虚函数(表)指针vfptr，指向vftable（虚函数表），表内记录虚函数的地址
v——virtual
f——function
ptr——pointer
tabel——表

父类虚函数表内记录虚函数的入口地址：
vftable
————————————————————————
| &Animal::speak
|
|
|

子类继承父类时，同时会继承一份父类的虚函数指针/虚函数表（与父类的一致）
当子类重写父类的虚函数后，子类中的虚函数表内部会替换成子类的虚函数地址
子类的虚函数表
vftable
————————————————————————
| &Cat::speak
|
|
|

当父类的指针或引用指向子类的对象时，发生多态：
Animal &animal = cat;
animal.speak();  // 它会走cat虚函数表中的speak地址

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

void test02()
{
    // 如果只有普通成员函数，是空类，只有1个字节，因为成员函数不属于类对象，且是分开存储的
    // 如果只有一个虚函数，则有8个字节，因为多存储了一个指针（vfptr）
    cout << "sizeof Animal = " << sizeof(Animal) << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}