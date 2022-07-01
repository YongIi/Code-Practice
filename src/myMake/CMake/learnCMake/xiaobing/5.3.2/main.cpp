#include "swap.h"

int main()
{
    swap mySwap(10, 20);
    mySwap.printInfo();
    mySwap.run();
    mySwap.printInfo();
    return 0;
}