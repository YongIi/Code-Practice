#pragma once
#include <string>
#include "../include/Gun.h"

class Soldier
{
public:
    Soldier(std::string name);
    ~Soldier();
    void addGun(Gun *ptr_gun);
    void addBulletToGun(int num);
    bool fire();

private:
    std::string _name;
    Gun *_ptr_gun;
};