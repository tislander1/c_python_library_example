#imports add_two function from ctypes

import ctypes

# Load the shared library (DLL)
twolib = ctypes.CDLL('./add_two.dll')

# use the float version of the function
my_float = 3.5
twolib.add_two_c.argtypes = [ctypes.c_float] # specify argument types
twolib.add_two_c.restype = ctypes.c_float  # specify result type
result = twolib.add_two_c(my_float) # call the function
print(f"The result of adding two to 3.5 is: {result}")


# use the list version of the function
my_list = [1.0, 4.0, 5.9]
twolib.add_two_array_c.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]  # specify argument types
twolib.add_two_array_c.restype = ctypes.POINTER(ctypes.c_double)  #
# Convert the Python list to a ctypes array of doubles
c_array = (ctypes.c_double * len(my_list))(*my_list)
# Call the function
result_array = twolib.add_two_array_c(c_array, len(my_list))
# Convert the result back to a Python list
result_list = [result_array[i] for i in range(len(my_list))]
print(f"The result of adding two to each element of {my_list} is: {result_list}")
x = 2


# add_two_strings function
string1, string2 = "Hello, ", "World!"

# Define the argument types and return type of the C function
twolib.add_two_strings_c.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
twolib.add_two_strings_c.restype = ctypes.c_char_p

#convert Python strings to byte strings
c_string1 = ctypes.c_char_p(string1.encode('utf-8'))
c_string2 = ctypes.c_char_p(string2.encode('utf-8'))
concatenated_string_ptr = twolib.add_two_strings_c(c_string1, c_string2)
# Convert the result back to a Python string
concatenated_string = concatenated_string_ptr.decode('utf-8')
print(f"The result of adding two strings '{string1}' and '{string2}' is: '{concatenated_string}'")

x = 2
