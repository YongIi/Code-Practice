#include <stdio.h>
#include "add.h"

int main()
{
    int a, b, c;
    a = 1;
    b = 5;

    add(&a, &b, &c);

    printf("%d\n", c);

    return 0;
}