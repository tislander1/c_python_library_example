#imports add_two function from ctypes

import ctypes

add_two_lib = ctypes.CDLL('./add_two.dll')
add_two_lib.add_two.argtypes = [ctypes.c_float] # specify argument types
add_two_lib.add_two.restype = ctypes.c_float  # specify result type

result = add_two_lib.add_two(3.5)

print(f"The result of adding two to 3.5 is: {result}")