# Python Interview Questions

---

## 1. What is the difference between a Module and a Package?

| Feature | Module | Package |
|------|------|------|
| **Definition** | A module is a single Python file containing functions, classes, or variables. | A package is a collection of related modules organized inside a directory. |
| **Example** | `math_operations.py` | `mypackage/` containing `__init__.py`, `math_operations.py`, `string_operations.py` |
| **Import example** | `import math_operations` | `from mypackage import math_operations` |

> **Interview tip:**  
> Every package is a module, but not every module is a package.

---

## 2. Is Python a compiled language or an interpreted language?

Python is **both compiled and interpreted**.

### Definitions

- **Compiled language**  
  A programming language where human-readable code is translated ahead of time into machine code.  
  Examples: C, C++, Rust, Go

- **Interpreted language**  
  Code is executed line by line at runtime.

---

### How Python Works

1. **Compilation Step**  
   Python source code (`.py`) is compiled into **bytecode** (`.pyc`) and stored in the `__pycache__` directory.
2. **Interpretation Step**  
   The bytecode is executed by the **Python Virtual Machine (PVM)**.

---

### What is the Python Virtual Machine (PVM)?

The PVM is the runtime engine that executes Python bytecode.

**Execution flow:**
1. You write Python code (`.py`)
2. Python compiler converts it to bytecode (`.pyc`)
3. PVM executes the bytecode instruction by instruction

---

### What the PVM does

- Reads bytecode instructions
- Executes operations (arithmetic, function calls, memory handling)
- Manages runtime environment (stack, namespaces, heap)
- Supports dynamic features (duck typing, dynamic binding)

---

### What is Bytecode?

Bytecode is an **intermediate, low-level, platform-independent** representation of Python code.

#### Why bytecode exists

- Faster than parsing source code repeatedly
- Platform independent
- Compact and optimized for execution

Example:

```python
x = 5 + 3

Bytecode (human-readable form):

LOAD_CONST    0 (5)
LOAD_CONST    1 (3)
BINARY_ADD
STORE_NAME    0 (x)
```
> **Interview tip:**  
> Python compiles source code into bytecode and then interprets it using the PVM.

## 3. What are the benefits of using Python in the present scenario?
1. Simplicity and readability
2. Versatility (web development, ML, data science, automation, DevOps)
3. Extensive libraries and frameworks
4. Strong community support
5. Portability
6. Fast development speed
7. Dynamic typing
8. Open source

> **Interview tip:**  
> Python prioritizes developer productivity over raw execution speed.

## 4. What are global, protected, and private attributes in Python?
Python does not enforce access control strictly. These are naming conventions, not true access modifiers.

### 1. Global (Public) Attributes
Accessible from anywhere

No underscore prefix

```python
class User:
    name = "Aastha"

print(User.name)
```

### 2. Protected Attributes (_variable)
Intended for internal use within a class or its subclasses

Still accessible outside the class (convention only)

```python
class User:
    def __init__(self):
        self._age = 23

class Admin(User):
    def show_age(self):
        print(self._age)
```

### 3. Private Attributes (__variable)
Name-mangled by Python to prevent accidental access

Not accessible directly outside the class

```python
class User:
    def __init__(self):
        self.__salary = 50000


u = User()
# print(u.__salary)   # AttributeError
print(u._User__salary)  # Name mangling
```


### Summary Table
| Type |Prefix|	Accessibility |
|------|------|------|
|Public	|variable	|Anywhere|
|Protected	|_variable	|Class & subclasses (convention)|
|Private	|__variable	|Class only (name mangling)|

> **Interview one-liner:**
> Python uses naming conventions rather than strict access modifiers.

## 5. Python Classes: 

### What is a class? 
A class is a blueprint. Not the actual thing - just the design of the thing 

Example:
- 🏠 Blueprint → shows rooms, doors, windows
- 🏠 House → actual building

In Python:
- Class → blueprint
- Object → actual thing created from it

> Interview : 
> A class is a blueprint that defines the structure and behavior of objects, and an object is an instance created from that class.

### Key Terms: 
| Term | Meaning | 
|------|---------|
|Class | Blueprint| 
|Object / Instance | Real things created from class | 
|Attribute | Data stored in object | 
|Method | Function that belongs to class | 
|```self```| Reference to current object | 

👉 Variables = data </br>
👉 Functions = actions</br>
👉 Classes = data + actions bundled together</br>

### What is ```self``` and why does it exist?
Think of ```self``` as "the current object" 

When you write: 
```python 
class Cookie: 
    def __init__(self,color):
        self.color = color
```
and then create object like 
```python
c1 = Cookie("red")
c2 = Cookie("blue")
```
Python automatically translate this behind the scenes: 
```python
Cookie.__init__(c1, "red")
Cookie.__init__(c2,"blue")
```
So: 
- ```self``` -> ```c1``` (first object)
- ```self``` -> ```c2``` (second object)

👉 self is just a reference to which object is calling the method.

Without self, Python wouldn’t know whether it’s dealing with c1, c2, or any other object.