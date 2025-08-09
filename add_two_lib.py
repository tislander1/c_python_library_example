#imports add_two function from ctypes

import ctypes

# Load the shared library (DLL)
class AddTwoLib:
    def __init__(self, lib_path):
        self.lib = ctypes.CDLL(lib_path)

    def add_two_float(self, number):
        self.lib.add_two_c.argtypes = [ctypes.c_float]
        self.lib.add_two_c.restype = ctypes.c_float
        return self.lib.add_two_c(number)
    
    def add_two_to_a_list(self, list1):
        self.lib.add_two_array_c.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]  # specify argument types
        self.lib.add_two_array_c.restype = ctypes.POINTER(ctypes.c_double)  #
        # Convert the Python list to a ctypes array of doubles
        c_array = (ctypes.c_double * len(list1))(*list1)
        # Call the function
        result_array = self.lib.add_two_array_c(c_array, len(list1))
        # Convert the result back to a Python list
        result_list = [result_array[i] for i in range(len(list1))]
        return result_list

    def add_two_strings(self, str1, str2):
        c_string1 = ctypes.c_char_p(str1.encode('utf-8'))
        c_string2 = ctypes.c_char_p(str2.encode('utf-8'))
        self.lib.add_two_strings_c.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.add_two_strings_c.restype = ctypes.c_void_p
        concatenated_string_ptr = self.lib.add_two_strings_c(c_string1, c_string2)
        concatenated_string = ctypes.string_at(concatenated_string_ptr).decode('utf-8')
        # Use the DLL's free function
        self.lib.free_c_string.argtypes = [ctypes.c_void_p]
        self.lib.free_c_string.restype = None
        self.lib.free_c_string(concatenated_string_ptr)
        return concatenated_string
    
    def add_two_lists_python(self, list1, list2, offset1, offset2):
        # add two lists with offsets.  If the lists are not the same length,
        # or do not overlap in certain areas, the value of the input list will be assumed to be 0
        # use python, not C, to do this
        min_position = min(offset1, offset2)
        max_position = max(offset1+ len(list1), offset2 + len(list2))

        result = []
        for i in range(min_position, max_position):
            value1 = list1[i - offset1] if (i - offset1) < len(list1) and (i - offset1) >= 0 else 0
            value2 = list2[i - offset2] if (i - offset2) < len(list2) and (i - offset2) >= 0 else 0
            result.append(value1 + value2)
        return result
    
    def add_two_lists(self, list1, offset1, list2, offset2):
        # add two lists with offsets using C.  If the lists are not the same length,
        # or do not overlap in certain areas, the value of the input list will be assumed to be 0

        # Define the argument and return types for the C function
        self.lib.add_two_lists_c.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, 
                                              ctypes.POINTER(ctypes.c_double), ctypes.c_int, 
                                              ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.lib.add_two_lists_c.restype = ctypes.POINTER(ctypes.c_double)

        # Convert the Python lists to ctypes arrays of doubles
        c_array1 = (ctypes.c_double * len(list1))(*list1)
        c_array2 = (ctypes.c_double * len(list2))(*list2)
        out_length = ctypes.c_int() # This will hold the length of the output array

        # Call the function
        result_array = self.lib.add_two_lists_c(c_array1, offset1,  c_array2,  offset2,
                                                len(list1), len(list2), ctypes.byref(out_length))
        # Convert the result back to a Python list
        result_list = [result_array[i] for i in range(out_length.value)]
        
        # Free the result array if necessary (depends on the C library implementation)
        self.lib.free_double_array.argtypes = [ctypes.POINTER(ctypes.c_double)]
        self.lib.free_double_array.restype = None
        self.lib.free_double_array(result_array)

        return result_list

if __name__ == "__main__":

    # Create an instance of the AddTwoLib class
    a2l = AddTwoLib('./add_two.dll')

    # add two to a float function
    my_float = 3.5
    result = a2l.add_two_float(my_float)
    print(f"The result of adding two to 3.5 is: {result}")

    # add two to a list function
    my_list = [1.0, 4.0, 5.9]
    result_list = a2l.add_two_to_a_list(my_list)
    print(f"The result of adding two to each element of {my_list} is: {result_list}")
    x = 2

    # add two strings function
    string1, string2 = "Add ", "two!"
    concatenated_string = a2l.add_two_strings(string1, string2)
    print(f"The result of adding two strings '{string1}' and '{string2}' is: '{concatenated_string}'")

    # add two lists with offsets using both Python and C
    # Define two lists and their offsets
    listA = [1.0, 2.0, 3.0]
    listB = [4.0, 5.0, 6.0]
    offsetA = 2
    offsetB = 4

    # add two lists with offsets using Python only
    result = a2l.add_two_lists_python(listA, listB, offsetA, offsetB)
    print(f"The result of adding {listA} and {listB} with offsets {offsetA} and {offsetB} using Python is: {result}")

    # add two lists with offsets using C
    result2= a2l.add_two_lists(listA, offsetA, listB, offsetB)
    print(f"The result of adding {listA} and {listB} with offsets {offsetA} and {offsetB} using C is: {result2}")
    