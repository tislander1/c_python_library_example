#imports add_two function from ctypes

import ctypes

# Load the shared library (DLL)
twolib = ctypes.CDLL('./add_two.dll')

# use the float version of the function
my_float = 3.5
twolib.add_two.argtypes = [ctypes.c_float] # specify argument types
twolib.add_two.restype = ctypes.c_float  # specify result type
result = twolib.add_two(my_float) # call the function
print(f"The result of adding two to 3.5 is: {result}")


# use the list version of the function
my_list = [1.0, 4.0, 5.9]
twolib.add_two_array.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]  # specify argument types
twolib.add_two_array.restype = ctypes.POINTER(ctypes.c_double)  #
# Convert the Python list to a ctypes array of doubles
c_array = (ctypes.c_double * len(my_list))(*my_list)
# Call the function
result_array = twolib.add_two_array(c_array, len(my_list))
# Convert the result back to a Python list
result_list = [result_array[i] for i in range(len(my_list))]
print(f"The result of adding two to each element of {my_list} is: {result_list}")
x = 2


x = 2
