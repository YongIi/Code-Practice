#pragma once
#include <iostream>
using namespace std;

class student
{
public:
    void setName(string getName);

    void setID(int getID);

    void printStudInfo();

public:
    string m_name;
    int m_ID;
};