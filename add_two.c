// compile add_two.c to a dll file with mingw, which can be used in Python with ctypes
//    gcc -shared -o add_two.dll add_two.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h> // For malloc

// Function to add 2.0 to a float number
float add_two_c(float number) {
    return number + 2.0;
}

// Function to add 2.0 to each element of a double array
double* add_two_array_c(double* arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] += 2.0;
    }
    return arr; // Return the pointer to the modified array
}

// Function to concatenate two strings
char* add_two_strings_c(const char* s1, const char* s2) {
    // Calculate the length of the new string
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    size_t total_len = len1 + len2 + 1; // +1 for null terminator

    // Allocate memory for the new string
    char* result = (char*)malloc(total_len);
    if (result == NULL) {
        return NULL; // Handle memory allocation failure
    }
    // Copy s1 to result
    strcpy(result, s1);
    // Concatenate s2 to result
    strcat(result, s2);
    return result;
}