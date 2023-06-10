#include <iostream>
#include <string>
using namespace std;

/*
多态案例三——电脑组装

电脑主要组成部件为 CPU（用于计算），显卡（用于显示），内存条（用于存储）

将每个零件封装出抽象基类，并且提供不同的厂商生产不同的零件，例如Intel厂商和Lenovo厂商

创建电脑类提供让电脑工作的函数，并且调用每个零件工作的接口

测试时组装三台不同的电脑进行工作

*/

// 抽象不同零件类
// 抽象CPU类
class CPU
{
public:
    // 抽象的计算函数
    virtual void calculate() = 0;
};

// 抽象GPU类
class GPU
{
public:
    // 抽象的显示函数
    virtual void display() = 0;
};

// 抽象内存条类
class Memory
{
public:
    // 抽象的存储函数
    virtual void storage() = 0;
};

class Computer
{
public:
    Computer(CPU *cpu, GPU *gpu, Memory *mem)
    {
        m_cpu = cpu;
        m_gpu = gpu;
        m_mem = mem;
    }

    // 提供工作的函数
    void work()
    {
        // 让零件工作起来，调用接口
        m_cpu->calculate();
        m_gpu->display();
        m_mem->storage();
    }

    // 提供一个析构函数来释放三个电脑的零件
    ~Computer()
    {
        if (m_cpu != NULL)
        {
            delete m_cpu;
            m_cpu = NULL;
        }

        if (m_gpu != NULL)
        {
            delete m_gpu;
            m_gpu = NULL;
        }

        if (m_mem != NULL)
        {
            delete m_mem;
            m_mem = NULL;
        }
    }

private:
    CPU *m_cpu;    // CPU的零件指针
    GPU *m_gpu;    // GPU的零件指针
    Memory *m_mem; // Memory的零件指针
};

// 具体厂商
// Intel厂商
class IntelCPU : public CPU
{
public:
    // 抽象的计算函数
    virtual void calculate() // 子类重写父类的虚函数
    {
        cout << "Intel的CPU开始计算了！" << endl;
    }
};

class IntelGPU : public GPU
{
public:
    // 抽象的显示函数
    virtual void display() // 子类重写父类的虚函数
    {
        cout << "Intel的GPU开始显示了！" << endl;
    }
};

class IntelMemory : public Memory
{
public:
    // 抽象的存储函数
    virtual void storage() // 子类重写父类的虚函数
    {
        cout << "Intel的内存条开始存储了！" << endl;
    }
};

// Lenovo厂商
class LenovoCPU : public CPU
{
public:
    // 抽象的计算函数
    virtual void calculate() // 子类重写父类的虚函数
    {
        cout << "Lenovo的CPU开始计算了！" << endl;
    }
};

class LenovoGPU : public GPU
{
public:
    // 抽象的显示函数
    virtual void display() // 子类重写父类的虚函数
    {
        cout << "Lenovo的GPU开始显示了！" << endl;
    }
};

class LenovoMemory : public Memory
{
public:
    // 抽象的存储函数
    virtual void storage() // 子类重写父类的虚函数
    {
        cout << "Lenovo的内存条开始存储了！" << endl;
    }
};

void test01()
{
    // 第一台电脑零件
    CPU *intelCPU = new IntelCPU;
    GPU *intelGPU = new IntelGPU;
    Memory *intelMem = new IntelMemory;

    cout << "第一台电脑开始工作：" << endl;
    // 创建第一台电脑
    Computer *computer1 = new Computer(intelCPU, intelGPU, intelMem);
    computer1->work();
    delete computer1;

    // 创建第二台电脑
    cout << "------------------" << endl;
    cout << "第二台电脑开始工作：" << endl;
    Computer *computer2 = new Computer(new LenovoCPU, new LenovoGPU, new LenovoMemory);
    computer2->work();
    delete computer2;

    // 创建第三台电脑
    cout << "------------------" << endl;
    cout << "第三台电脑开始工作：" << endl;
    Computer *computer3 = new Computer(new LenovoCPU, new IntelGPU, new LenovoMemory);
    computer3->work();
    delete computer3;
}

int main()
{
    test01();
    return 0;
}