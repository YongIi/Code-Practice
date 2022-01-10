#include <iostream>
using namespace std;

class student
{
public:
    void setName(string getName)
    {
        m_name = getName;
    }
    void setID(int getID)
    {
        m_ID = getID;
    }
    void printStudInfo()
    {
        cout << "student name:" << m_name << '\t' << "student ID:" << m_ID << endl;
    }

public:
    string m_name;
    int m_ID;
};

int main()
{
    student stu;
    stu.setName("Noxus");
    stu.setID(007);
    stu.printStudInfo();
    return 0;
}