# Exception Handling


Exceptions are raised by Python when it can't interpret what your program is trying to do. You can read more about exceptions in the [official docs](https://docs.python.org/3.6/tutorial/errors.html).


<table>
<tr>
<td width="40%">

For example, the following occurs when we attempt to concatenate a string an an int (e.g. `print('your age is: ' + 23)`)

</td>
<td width="60%">

```python
Traceback (most recent call last):
    MORE FUNCTIONS...
    File "test.py", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

</td>
</tr>
</table>


## Exceptions

Exceptions can occur for many different reasons: poorly formatted code, referring to objects and attributes that don't exist, passing the wrong types of parameters to functions, etc. When you get an error be sure to read the message and what line it occurred on. Some common exceptions are below. You can read more about Python exceptions [here](https://www.tutorialsteacher.com/python/error-types-in-python).



### SyntaxError
<table>
<tr>
<td width="40%">

A SyntaxError occurs if your code is poorly formatted.

</td>
<td width="60%">

```python
if: # SyntaxError: invalid syntax
```

</td>
</tr>
<tr>
<td>

**SyntaxError: invalid syntax**

</td>
<td>

```python
print(
```

</td>
</tr>
</table>




### IndentationError

<table>
<tr>
<td width="40%">

An IndentationError occurs when a block (`if`, `elif`, `else`, `while`, `for`, `with`, etc) has improper indentation.

</td>
<td width="60%">

```python
if True:
print('hi') # IndentationError: expected an indented block

if 5 < 10:
        print('test')
    print('test 2') # IndentationError: unindent does not match any outer indentation level
```

</td>
</tr>
</table>



### NameError

<table>
<tr>
<td width="40%">

A NameError occurs when one attempts to use a variable or call a function that has not been defined. This often happens when a variable or function is misspelled, or used before it's declared.

</td>
<td width="60%">

```python
print(a) # NameError: name 'a' is not defined
a() # NameError: name 'a' is not defined
a + 1 # NameError: name 'a' is not defined
```

</td>
</tr>
</table>



### AttributeError

<table>
<tr>
<td width="40%">

An AttributeError occurs when one attempts to access a property or method that does not exist that does not exist.

</td>
<td width="60%">

```python
x = 5
x.myprop # AttributeError: 'int' object has no attribute 'myprop'
x.mymethod() # AttributeError: 'int' object has no attribute 'mymethod'
```

</td>
</tr>
</table>


### TypeError

```python
age = 23
age[0] # TypeError: 'int' object is not subscriptable
'your age is ' + age # TypeError: can only concatenate str (not "int") to str
len(age) # TypeError: object of type 'int' has no len()
```


### IndexError

<table>
<tr>
<td width="40%">

An IndexError occurs when you try to access an element of a list using an index that's out of range.

</td>
<td width="60%">

```python
nums = [1, 2, 3]
print(nums[3]) # IndexError: list index out of range
```

</td>
</tr>
</table>

### KeyError

<table>
<tr>
<td width="40%">

A KeyError occurs when you try to access a key that's not in a dictionary.

</td>
<td width="60%">

```python
d = {'a':1, 'b':2, 'c':3}
print(d['d']) # KeyError: 'd'
```

</td>
</tr>
</table>



### ValueError

<table>
<tr>
<td width="40%">

A ValueError occurs when you try to perform an invalid type conversion.

</td>
<td width="60%">

```python
x = int('hi') # ValueError: invalid literal for int() with base 10: 'hi'
```

</td>
</tr>
</table>




## Raising Exceptions

<table>
<tr>
<td width="40%">

When an exception is raised, the function returns, and no code after it will be run. If the exception is not caught, it causes the program to crash and is printed to the user.

</td>
<td width="60%">

```python
def crash(i):
    if i < 0:
        raise ValueError('i cannot be less than 0')
    print('continuing on...')
```

</td>
</tr>
</table>



## Catching Exceptions

<table>
<tr>
<td width="40%">

You can catch exceptions that are raised by wrapping the code that may raise them in a try-except block. When the code throws an exception, any code after it won't be executed. [Is This Best Practice?](https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python)

</td>
<td width="60%">

```python
try:
    this_wont_work = 1 + 'hello'
    this_wont_be_run()
except TypeError:
    print('That didn\'t work!')
```

</td>
</tr>
<tr>
<td width="40%">

A common exception you might want to handle is when you try to access a key that doesn’t exist in a dictionary.

</td>
<td width="60%">

```python
my_dict = {'foo':'bar'}
try:
    my_value = my_dict['baz']
except KeyError:
    print('Try again!')
```

</td>
</tr>
<tr>
<td width="40%">

Another use-case is checking if the user entered a valid integer:

</td>
<td width="60%">

```python
while True:
    try:
        x = int(input('enter a number: '))
        break
    except ValueError:
        print('try again')
print(x)
```

</td>
</tr>
<tr>
<td width="40%">

If you want to catch multiple exceptions, use a tuple, or use multiple blocks.

</td>
<td width="60%">

```python
import random

 # using a tuple
try:
    if random.randint(0, 1) == 0:
        raise KeyError('index error')
    else:
        raise IndexError('key error')
except (KeyError, IndexError) as e:
    print(e)
    print(type(e) == KeyError)
    print(type(e) == IndexError)

 # using multiple except blocks
try:
    if random.randint(0, 1) == 0:
        raise IndexError('index error')
    else:
        raise KeyError('key error')
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
```

</td>
</tr>
<tr>
<td width="40%">

You can also leave the type of exception absent, which will catch all exceptions.

</td>
<td width="60%">

```python
try:
    # some stuff
except: # catch anything!
    # handle error
```

</td>
</tr>
</table>

## Else and Finally

<table>
<tr>
<td width="40%">

An optional else block may be added to the end of a try-catch block as well. The else block is executed if no exception is thrown.

An optional finally block comes last. It is guaranteed to execute whether or not a exception is thrown. This is useful for closing files.

</td>
<td width="60%">

```python
try:
    f = open('file.txt')
    contents = f.read()
    print(contents)
except (IOError, OSError) as e:
    print(e)
else:
    print('no exception occurred')
finally:
    f.close()
```

</td>
</tr>
</table>

## Writing Custom Exceptions

<table>
<tr>
<td width="40%">

You can write your own exceptions by writing a custom [class](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/1%20Python/docs/15%20-%20Classes.md) for it and inheriting from `Exception`. This is useful if you had a particular name for your exception, or wanted it to carry particular information.

</td>
<td width="60%">

```python
class MyException(Exception):
    def __init__(self, text, id):
        super().__init__(text)
        self.id = id

try:
    raise MyException('hi', 5)
except MyException as e:
    print(e.id)
```

</td>
</tr>
</table>

## Testing

<table>
<tr>
<td width="40%">

We can use the `pytest` module to write test code for our functions. First run `pip install pytest` to install the library. Then write a function to test and a separate 'test' method which has the function name but `test_` in front. Finally, run `pytest example.py`, which should run all the tests and tell you if any failed.


</td>
<td width="60%">

> `pytest add.py`

```python
# add.py
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(5, 2) == 7
```

</td>
</tr>
</table>
