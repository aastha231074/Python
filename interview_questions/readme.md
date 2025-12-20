# Python Interview Questions 

## 1. What is the difference between a Module and a Package? 
| Feature  | Module  | Package  |   
|---|---|---|
|   Definition | A module is a single Python file that contains code like functions, classes and valriables.  |  A package is a collection of modules organised in a directory |   
| Example  | `math_operations.py`  | `mypackages/` with `__init__.py` , `math_operations.py`, `string_operations.py` |   
| Import example  | import math_operations.py  |  from mypackage import math_operations |   

## 2. Is Python a compiled language or an interpreted language? 
- <b>Compiled language</b> is a programming lanuage where human-read-able code is translated ahead of time by a compiler into low level machine code ( binary ) that a computer's CPU can execute directly. e.g. C, C++, Rust, Go

- <b> Interpreted language </b> translate line by line at runtime 

    Python is generally considered an interpreted language, but the reality it's actaully a both compiled and interpreted

    ### How Python Works? 
    1. Compilation Step: When you run a Python program, the source code (`.py` files) is first compiled into bytecode ( `.pyc` file stored in `__pycache__`). This bytecode is a lower-level, platform-intependent representation of your code.
    2. Interpretation Step: The byte code is then executed by the Python Virtual Machine, which interprets it line by line. 

    ### What is Python Virtual Machine?
    The Pyton Virtual Machine is the runtime engine that actually executes Python bytecode.
    1. You write python code (`.py` file)
    2. Python compiler converts it to bytecode (`.pyc` file)
    3. PVM reads and executes the bytecode instruction by instruction 

    #### What the PVM does:
    The PVM is essentially an interpreter loop that:

    - Reads bytecode instructions one at a time
    - Performs the corresponding operations (like adding numbers, calling functions, managing memory)
    - Maintains the runtime environment (stack, namespace, memory)
    - Handles Python's dynamic features (duck typing, dynamic binding)


    ### What is byte code?
    Byte Code is an intermediate low level representaion of your code that sits between human-readable source code and machine code.  
    #### Why bytecode exists:
    Python source code is too high-level for computers to execute directly, but compiling all the way to machine code would make Python lose its portability and dynamic features. Bytecode is the compromise—it's:

    - Faster to execute than parsing source code repeatedly
    - Platform-independent (works on any OS with Python installed)
    - Compact (smaller than source code)
    
    ```python 
        x = 5 + 3
        ```
        **Bytecode (human-readable form):**
        ```
        LOAD_CONST    0 (5)
        LOAD_CONST    1 (3)
        BINARY_ADD
        STORE_NAME    0 (x)
    ```



## 3. What are the benefits of using Python language as a tool in the present scenario? 
1. Simplicity 
2. Versality 
3. Extensive libraries and framework
4. Strong community support 
5. Portability
6. Development Speed 
7. Dynamic Typing 
8. Open Source 

## 4. What are global, protected and private attributes in Python? 
- <b> Global </b> variables are public variables defined 

