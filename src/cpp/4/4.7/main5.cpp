#include <iostream>
#include <string>
using namespace std;

/*
制作饮品案例

冲咖啡————————————冲茶叶
1、煮水          1、煮水
2、冲泡咖啡      2、冲泡茶叶
3、倒入杯中      3、倒入杯中
4、加糖和牛奶    4、加柠檬

利用多态技术实现本案例，提供抽象制作饮品基类，提供子类制作咖啡和茶叶
*/

class AbstractDrinking
{
public:
    // 煮水
    virtual void Boil() = 0;
    // 冲泡
    virtual void Brew() = 0;
    // 倒入杯中
    virtual void PourInCup() = 0;
    // 倒入辅料
    virtual void PutSomething() = 0;

    // 制作饮品
    void makeDrink()
    {
        Boil(); // 以下都是去子类寻找具体是实现
        Brew();
        PourInCup();
        PutSomething();
    }
};

// 制作咖啡
class Coffee : public AbstractDrinking
{
public:
    // 煮水
    virtual void Boil()
    {
        cout << "煮水" << endl;
    }
    // 冲泡
    virtual void Brew()
    {
        cout << "冲泡咖啡" << endl;
    }
    // 倒入杯中
    virtual void PourInCup()
    {
        cout << "倒入杯中" << endl;
    }
    // 倒入辅料
    virtual void PutSomething()
    {
        cout << "加入糖和牛奶" << endl;
    }
};

// 制作茶叶
class Tea : public AbstractDrinking
{
public:
    // 煮水
    virtual void Boil()
    {
        cout << "煮水" << endl;
    }
    // 冲泡
    virtual void Brew()
    {
        cout << "冲泡茶叶" << endl;
    }
    // 倒入杯中
    virtual void PourInCup()
    {
        cout << "倒入杯中" << endl;
    }
    // 倒入辅料
    virtual void PutSomething()
    {
        cout << "加入柠檬" << endl;
    }
};

// 制作饮品函数
void doWork(AbstractDrinking *abs) // 同一个接口，可以实现不同的功能（做不同的饮品）
{
    abs->makeDrink();
    delete abs;
}

void test01()
{
    // 制作咖啡
    doWork(new Coffee);

    cout << "-----------" << endl;

    // 制作茶水
    doWork(new Tea);
}

int main()
{
    test01();
    return 0;
}