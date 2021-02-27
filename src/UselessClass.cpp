#include "UselessClass.h"

#include <iostream>

using useless_lib::UselessClass;

int UselessClass::Sum(int x, int y)
{
    return x + y;
}

void UselessClass::HelloWorld()
{
    std::cout << "Hello World From Useless Lib!" << std::endl;
}
