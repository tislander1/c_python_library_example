#include <stdio.h>

float add_two(float number) {
    return number + 2.0;
}

// compile add_two.c to a dll file with mingw:
//    gcc -shared -o add_two.dll add_two.c
