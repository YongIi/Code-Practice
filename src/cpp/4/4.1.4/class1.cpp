#include "class1.h"

void student::setName(string getName)
{
    m_name = getName;
}
void student::setID(int getID)
{
    m_ID = getID;
}
void student::printStudInfo()
{
    cout << "student name:" << m_name << '\t' << "student ID:" << m_ID << endl;
}
