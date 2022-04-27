#include <iostream>
#include <string>
using namespace std;

//继承中的对象模型
class Base
{
public:
    int m_A;

protected:
    int m_B;

private:
    int m_C;
};

class Son : public Base
{
public:
    int m_D;
};

//在Windows系统中若使用VS工具，可以利用开发人员命令提示工具查看对象模型
//1，跳转盘符 F：
//2，跳转文件路径cd具体路径下
//查看命令：
//cl /d1 reportSingleClassLayout类名 所属的文件名

void test01()
{
    //父类中所有的非静态成员属性都会被子类继承下去
    //父类中私有成员属性是被编译器给隐藏了，因此是访问不到，但确实是被继承下去了
    cout << "size of Son = " << sizeof(Son) << endl;
}

int main()
{
    test01();
    return 0;
}