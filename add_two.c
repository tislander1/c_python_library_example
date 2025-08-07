#include <stdio.h>

// Function to add 2.0 to a float number
float add_two(float number) {
    return number + 2.0;
}


// Function to add 2.0 to each element of a double array
double* add_two_array(double* arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] += 2.0;
    }
    return arr; // Return the pointer to the modified array
}

// compile add_two.c to a dll file with mingw:
//    gcc -shared -o add_two.dll add_two.c
