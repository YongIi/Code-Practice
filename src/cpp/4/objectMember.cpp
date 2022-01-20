#include <iostream>
using namespace std;
#include <string>

// 类对象作为类成员

class Phone
{
public:
    Phone(string brand)
    {
        m_Brand = brand;
        cout << "Phone的构造函数调用" << endl; //当类嵌套时，查看先构造哪个对象
    }
    ~Phone()
    {
        cout << "Phone的析构函数调用" << endl; //当类嵌套时，查看先析构哪个对象
    }
    string m_Brand; //手机的品牌
};

class Person
{
public:
    //构造函数用于初始化对象，初始化列表用来初始化成员变量
    //初始化列表初始化时，调用了构造函数第3种初始化对象的方法，即隐式转换法，初始化对象时直接用=传入参数：类名 P3 = 100；
    //初始化列表中m_Name(name)相当于string m_Name = name;
    //m_Phone(brand)相当于Phone m_Phone = brand 即隐式转换法，类名 对象名 = 参数;
    Person(string name, string brand): m_Name(name), m_Phone(brand)
    {
        cout << "Person的构造函数调用" << endl; //当类嵌套时，查看先构造哪个对象 —— 创建本类时，会先创建其他类的对象
    }
    ~Person()
    {
        cout << "Person的析构函数调用" << endl; //当类嵌套时，查看先析构哪个对象 —— 零件组成手机，手机拆了才能拆零件
    }
    // 姓名
    string m_Name;
    // 手机
    Phone m_Phone;
};

//当其他类对象作为本类成员时，构造时先构造其他类的对象，再构建自身的对象；析构则相反，先构造的后释放， 母体释放了子体才能自由释放
void test01()
{
    Person p("张三", "苹果Max");
    cout << p.m_Name << "拿着" << p.m_Phone.m_Brand << "手机" << endl;
}

int main()
{
    test01();
    return 0;
}