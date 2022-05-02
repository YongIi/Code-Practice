#include <iostream>
#include <string>
using namespace std;

//动物类
class Animal
{
public:
    int m_Age;
};

//利用虚继承解决菱形继承的问题
//继承之前加上关键字virtual变为虚继承，此时Animal称为虚基类

//羊类
class Sheep : virtual public Animal
{
};

//驼类
class Tuo : virtual public Animal
{
};

//羊驼类
class SheepTuo : public Sheep, public Tuo
{
};

void test01()
{
    SheepTuo st;
    st.Sheep::m_Age = 18;
    st.Tuo::m_Age = 28;
    //当菱形继承时，两个父类拥有继承自祖父的相同数据，这个数据同名但两个父类都拥有，且数据值可以不相同，等同于多继承时不同父类有重名成员，需要加作用域来区分(该语句指的是不使用虚继承的情况下，此时下面的运行结果分别是18和28)
    cout << "st.Sheep::m_Age = " << st.Sheep::m_Age << endl;
    cout << "st.Tuo::m_Age = " << st.Tuo::m_Age << endl;
    //但这份数据其实只需要一份就可以了，菱形继承导致数据有两份的，导致资源浪费
    //采用虚继承后，只继承了一个数据，这个数据可以共享，使用st.Sheep::m_Age，st.Tuo::m_Age，st.m_Age都是访问的同一个数据
    cout << "st.m_Age = " << st.m_Age << endl;
    //虚继承本质
    //在虚继承时，Sheep和Tuo中继承下来的时vbptr，该指针会指向vbtable(记录偏移量),vbptr+vbtable之后都会指向同一个数据，故该数据是共享的
    // vbptr: virtual base pointer
}

int main()
{
    test01();
    return 0;
}