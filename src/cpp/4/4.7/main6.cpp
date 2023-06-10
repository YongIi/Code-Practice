#include <iostream>
#include <string>
using namespace std;

/*
虚析构和纯虚析构

使用条件：
多态使用时，父类的指针/引用指向子类对象，如果子类中有属性开辟到堆区，
那么父类指针在delete释放时（析构时）无法调用到子类的析构代码，造成内存泄漏
如果子类中没有堆区数据，可以不写虚析构和纯虚析构

解决方法：将父类中的析构函数改为虚析构或者纯虚析构

虚析构语法：
virtual ~类名(){函数实现}
纯虚析构语法：
virtual ~类名() = 0;
类名::~类名(){函数实现}

虚析构和纯虚析构共性：
1、可以解决父类指针释放子类（堆区）对象
2、都需要有具体的函数实现（虚析构函数内必须有内容，纯虚析构函数必须在类外 '类名::~类名(){}' 中填充内容）
3、不需要父类的析构函数与子类的析构函数同名，即并不是多态中的重写虚函数

虚析构与纯虚析构的区别：
如果是纯虚析构，该类属于抽象类，无法实例化对象

纯虚函数与纯虚析构的区别：
1、纯虚函数 父类中仅需要声明不需要实现。子类中重写虚函数时，函数名与父类中的函数名相同
2、纯虚析构 父类中需要声明也需要实现（类外实现）。子类中用自己的析构函数，析构函数名与子类类名相同


构造/析构顺序：
子类继承父类时，创建子类对象时构造和析构有先后顺序，
因为子类会继承父类的属性，也就需要用到父类的构造函数初始化赋值
先构造父类的属性再构造子类属性，即先调用父类构造函数，再调用子类构造函数
析构则相反，先析构子类的属性，再析构父类的属性，即先调用子类的析构函数，再调用父类的析构函数
先创造的后销毁

*/

class Animal
{
public:
    Animal()
    {
        cout << "Animal构造函数调用" << endl;
    }

    /*
    //利用虚析构可以解决父类指针释放子类对象时，堆区内存释放不干净的问题
    virtual ~Animal()
    {
        cout << "Animal虚析构函数调用" << endl;
    }
    */

    // 纯虚析构 需要声明也需要实现（类外实现）
    // 有了纯虚析构之后，这个类也属于抽象类，无法实例化对象
    virtual ~Animal() = 0;

    // 纯虚函数 仅需要声明不需要实现
    virtual void speak() = 0;
};

// 类外实现纯虚析构的实现
Animal::~Animal()
{
    cout << "Animal纯虚析构函数调用" << endl;
}

class Cat : public Animal
{
public:
    Cat(string name)
    {
        cout << "Cat的构造函数调用" << endl;
        m_Name = new string(name);
    }

    virtual void speak()
    {
        cout << *m_Name << "小猫在说话" << endl;
    }

    ~Cat()
    {
        if (m_Name != NULL)
        {
            cout << "Cat的析构函数调用" << endl;
            delete m_Name; // 释放的是堆区内存，指针m_Name自己没被delete
            m_Name = NULL;
        }
    }

    string *m_Name;
};

void test01()
{
    Animal *animal = new Cat("Tom");
    animal->speak();
    delete animal;
}

int main()
{
    test01();
    return 0;
}