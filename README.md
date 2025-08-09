# c_python_library_example
first example of a python library written in c

- AddTwoLib is a Ctypes python library that
    - Adds 2.0 to a float
    - Adds 2.0 to a list
    - Adds/combines two strings 
    - Adds two lists together, with possible offsets in the lists

- compile add_two.cpp to a dll file with mingw:
    g++ -shared -o add_two.dll add_two.cpp

