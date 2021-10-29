#include "Soldier.h"
#include "Gun.h"
#include <iostream>

void test()
{
    Soldier sanduo("xusanduo");
    sanduo.addGun(new Gun("AK47"));
    sanduo.addBulletToGun(20);
    sanduo.fire();
}

int main()
{
    std::cout << "testing..." << std::endl;
    test();
    std::cout << "ending..." << std::endl;
    return 0;
}