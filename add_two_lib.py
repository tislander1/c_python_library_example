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
    
    def add_two_list(self, list1):
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
        #convert Python strings to byte strings
        c_string1 = ctypes.c_char_p(str1.encode('utf-8'))
        c_string2 = ctypes.c_char_p(str2.encode('utf-8'))
        self.lib.add_two_strings_c.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.add_two_strings_c.restype = ctypes.c_char_p
        concatenated_string_ptr = self.lib.add_two_strings_c(c_string1, c_string2)
        # Convert the result back to a Python string
        concatenated_string = concatenated_string_ptr.decode('utf-8')
        return concatenated_string

if __name__ == "__main__":
    # Create an instance of the AddTwoLib class
    a2l = AddTwoLib('./add_two.dll')

    # add two to a float function
    my_float = 3.5
    result = a2l.add_two_float(my_float)
    print(f"The result of adding two to 3.5 is: {result}")

    # add two to a list function
    my_list = [1.0, 4.0, 5.9]
    result_list = a2l.add_two_list(my_list)
    print(f"The result of adding two to each element of {my_list} is: {result_list}")
    x = 2

    # add two strings function
    string1, string2 = "Add ", "two!"
    concatenated_string = a2l.add_two_strings(string1, string2)
    print(f"The result of adding two strings '{string1}' and '{string2}' is: '{concatenated_string}'")
