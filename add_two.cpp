// compile add_two.c to a dll file with mingw, which can be used in Python with ctypes
//    gcc -shared -o add_two.dll add_two.c

#include <cstdio>
#include <cstring>
#include <cstdlib> // For malloc


extern "C" {

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

    // Function to free memory allocated by add_two_strings_c
    void free_c_string(char* ptr) {
        free(ptr);
    }

    // Function to add two lists with offsets
    // The function takes two lists, their offsets, and their sizes, and returns a new list
    // that contains the sum of the two lists, taking into account the offsets.
    // The length of the output list is also returned through an out_length pointer.
    double* add_two_lists_c(double* list1, int offset1, double* list2, int offset2,
        int size1, int size2, int* out_length) {
        
        // the minimum offset is the start of the result list
        int min_offset = (offset1 < offset2) ? offset1 : offset2;

        // the maximum offset is the end of the result list
        int max_offset = (offset1 + size1 > offset2 + size2) ?
                         (offset1 + size1) : (offset2 + size2);

        // Calculate the maximum length of the result list
        int max_length = max_offset - min_offset;

        // If out_length is not NULL, set it to the maximum length
        // This will be returned through the out_length pointer
        if (out_length) *out_length = max_length;

        // Allocate memory for the result list
        double* result = (double*)malloc(max_length * sizeof(double));
        if (result == NULL) {
            if (out_length) *out_length = 0;
            return NULL; // Handle memory allocation failure
        }
        // Iterate through the range of the result list
        // and fill it with the sum of the two lists, considering the offsets
        for (int i = min_offset; i < min_offset + max_length; i++) {
            double value1 = (i - offset1 >= 0 && i - offset1 < size1) ? list1[i - offset1] : 0.0;
            double value2 = (i - offset2 >= 0 && i - offset2 < size2) ? list2[i - offset2] : 0.0;
            result[i - min_offset] = value1 + value2;
        }
        return result;
    }
    // Function to free memory allocated by add_two_lists_c
    void free_double_array(double* ptr) {
        free(ptr);
    }

}