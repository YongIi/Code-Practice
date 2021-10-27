#include <iostream>
#include "add.h"

int main()
{
    int x, y, z;
    x = 1;
    y = 3;
    z = add(&x, &y);
    std::cout << z << std::endl;
    return 0;
}