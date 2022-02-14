#include <iostream>
#include <string>
using namespace std;

//房屋
class Building
{
    //goodguy全局函数是Building好朋友，可以访问Building中私有成员
    friend void goodguy(Building *building);

public:
    Building()
    {
        m_SittingRoom = "客厅";
        m_BedRoom = "卧室";
    }

public:
    string m_SittingRoom; //客厅
private:
    string m_BedRoom; //卧室
};

//全局函数
void goodguy(Building *building)
{
    cout << "好基友全局函数正在访问：" << building->m_SittingRoom << endl;

    cout << "好基友全局函数正在访问：" << building->m_BedRoom << endl;
}

void test01()
{
    Building building;
    goodguy(&building);
}

int main()
{
    test01();
    return 0;
}