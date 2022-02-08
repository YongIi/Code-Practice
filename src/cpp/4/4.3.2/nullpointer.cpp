#include <iostream>
using namespace std;

//空指针调用成员函数
//用指针调用成员函数时，若成员函数用到了成员变量，则要用this帮助查看该指针p是否指向空指针：if(this==NULL){return；} 用于规避访问空指针的内存
class Person
{
public:
    void showClassName()
    {
        cout << "This is Person class" << endl; //没用到成员变量所以是安全的
    }

    void showPersonAge()
    {
        //如果不添加以下代码，用于调用的指针是为NULL时会报错，报错原因是因为空指针的内存不允许访问，并且空指针的指向没有实体，也访问不到里面的成员属性
        if(this == NULL)    //this是对象本身的地址，用this帮助查看该指针p是否指向空指针
        {
            return; //this查出是指向空指针时直接跳过该成员函数，预防被破坏导致程序崩掉
        }

        cout << "age = " << m_Age << endl;  //其实属性的前面都默认加了“this->m_Age”，只是隐藏了
    }

    int m_Age;
};

void test01()
{
    Person *p = NULL;   //空指针的指向没有实体

    p->showClassName();
    
    p->showPersonAge();   
}

int main()
{
    test01();
    return 0;
}