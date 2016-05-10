About this workshop 

We will experiment with the Python programming language and its capabilities.We'll go through this topics:
- Basic Syntax 
- Data Types ( int, float, lists, tuples ... )
- Built in functions( print, input, max ... )
- Control structures( if-elif-else, for, while ...)
- Library structure
- Objects and Classes (creating, inheritage )
- Built in libraries ( os, sys, copy, random, datetime ... )

Prerequisites
In this workshop we'll need :
- A laptop with Python 3.x installed 
- Past experience with any programming language ( basic concepts  )

What's in for you ?
After this workshop you will be familiarized with the Pythong programming language and its capabilities.You will be able to make your own helpfull scripts.

Micu Matei-Marius ( descriere )
I can describe myself as a guy who is really into most topics related to tehnology.I'm a tinkerer and a explorer when it comes to new and exciting topics.I have been experimenting  with coding for almost 5 years, and I would never give my linux and vim away for anything. 


---
## 1. Basic Sintax
```python
# comentariu pe o linie
# ...

"""
Comentariu pe 
mai 
multe 
linii ( e un string defapt )
"""

# atriburi
basic_int = 10
basic_string = "Some string"
long_string = """ Long string,
pe mai 
multe 
linii
"""

# ATENTIE LA indentare
x = 10 # valid
    x = 10 # eroare

```

---
## 2.  Data Types
```python
some_int = 10 

some_float = 10.2

some_string = "Some string"
another_string = """ Long string,

some_list = [1, 2, 3, 4]

some_tuple = (1, 2, 3)

```

### 2.2 More on Lists
```python
>>> l = [1, 2, 3]
>>> l[0]
1

>>> l[2]
3

>>> l[-1]
3

>>> l[-2]
2

>>> len(l)
3

>>> l[:2]
[1, 2]

>>> l[:3]
[1, 2, 3]

>>> l[-1:]
[3]

>>> l.append(8)
>>> l
[1, 2, 3, 8]

>>> l.extend([4, 5, 6, 7])
>>> l
[1, 2, 3, 8, 4, 5, 6, 7]

>>> l.sort()
>>> l
[1, 2, 3, 4, 5, 6, 7, 8]

>>> l.reverse()
>>> l
[8, 7, 6, 5, 4, 3, 2, 1]

```

### 2.3 Dictionare
```python
dictionar = {
    "first item" : [1, 2, 3],
    "second item": (1, 2, 3),
    "other items" :{
        1 : "Jon",
        2 : "Doe"
    }
}
```
---
## 3. Functii built-in
```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

```
---
