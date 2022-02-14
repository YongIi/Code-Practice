#include <iostream>
#include <string>
using namespace std;

//类做友元

class Building; //事先说明该类的存在

class goodGuy
{
public:
    goodGuy();
    void visit(); //参观函数访问Building中的属性
    Building *building;
};

class Building
{
    //告诉编译器goodGuy类是本类的好朋友，可以访问本类中的私有成员
    friend class goodGuy;

public:
    Building();

public:
    string m_SittingRoom; //客厅
private:
    string m_BedRoom; //卧室
};

//类外写成员函数
Building::Building()
{
    m_SittingRoom = "客厅";
    m_BedRoom = "卧室";
}

goodGuy::goodGuy()
{
    //创建建筑物对象
    building = new Building; //在堆区开辟对象，地址传给building //此处略去了析构函数delete掉该内存
}

void goodGuy::visit()
{
    cout << "好基友类正在访问：" << building->m_SittingRoom << endl;

    cout << "好基友类正在访问：" << building->m_BedRoom << endl;
}

void test01()
{
    goodGuy gg;
    gg.visit();
}

int main()
{
    test01();
    return 0;
}