<div style="max-width: 1000px; margin: 0 auto;">

# Fundamentals

## Variables, Objects, & Types
<table>
<tr>
<thead>

### Variables

</thead>

<tr>
<td width="40%">

Variables are names given to objects. These allow us to specify the operations we'd like to perform on that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables. You can get an identifier for an object with the function `id()`

</td>
<td width="60%">

```python
x = 5 # x is the variable, 5 is the object
print(id(x))
message = 'hello' # message is the variable, 'hello' is the object
print(id(message))
```
> 512341256<br>
> 231661621
</td>
</tr>
</table>

Everything is an object in python, including None, booleans, integers, floats, modules, classes, and functions. This means they can be assigned to variables, passes as parameters to functions, and be put into lists and dictionaries.


### Types
<table>
<tr>
<td width="40%">

Every object has a type, which can be checked by using the `type()` function.

</td>
<td width="60%">

```python
print(type(None)) # <class 'NoneType'>
print(type(False)) # <class 'boolean'>
print(type(5)) # <class 'int'>
print(type(5.0)) # <class 'float'>
print(type('hello')) # <class 'str'>
print(type(type(5))) # <class 'type'>
```

</td>
</tr>
<tr>
<td width="40%">

We can define custom types using [classes](#classes).

</td>
<td width="60%">

```python
class Point:
    def __init__(self):
        pass
p = Point()
print(type(p)) # <class '__main__.Point'>
print(type(Point)) # <class 'type'>
```

</td>
</tr>
</table>


### Literals

<table>
<tr>
<td width="40%">

The easiest way to enter data in your problem is through 'literals', which are called as such because they're *literally* written in the source code.

</td>
<td width="60%">

- bool literals: `True` and `False`
- int literals: `3`, `-20`, `294927`
- float literals: `3.2`, `3.14e-10`
- string literals: `'hello'` and `"world"`
- list literals: `[]`, `[1, 2, 3]`
- dict literals: `{}`, `{'a': 1, 'b': 2}`

</td>
</tr>
</table>



### Type Conversion

<table>
<tr>
<td width="40%">

Every type or class has an initializer, which can be used to create an instance of that class.

</td>
<td width="60%">

```python
print(bool('True')) # True
print(int('5')) # 5
print(float('5.0')) # 5.0
print(str(5)) # '5'
```

</td>
</tr>
</table>




### Mutability

<table>
<tr>
<td width="40%">

Certain datatypes in Python are **immutable** meaning their values **cannot** be changed. Immutable types include ints, floats, strings, and tuples. This is why string methods like `lower`, `replace` and `strip` return **copies** of the given string. [stack overflow](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)

</td>
<td width="60%">


```python
x = 5
y = x
y += 2
print(x) # 5
print(y) # 7
```

```python
x = ['apples', 'bananas', 'pears']
y = x
y.append('cherries')
print(x) # ['apples', 'bananas', 'pears', 'cherries']
print(y) # ['apples', 'bananas', 'pears', 'cherries']
```
</td>
</tr>
</table>


## I/O

### Print

<table>
<tr>
<td width="40%">

Print is a function in python that allows us to print text to the terminal. Each call to `print` will output whatever's passed as a parameter to the console. [python docs](https://docs.python.org/3/library/functions.html#print)

</td>
<td width="60%">

```python
print('hello')
print('world')
```
> hello<br>
> world

</td>
</tr>
</table>


#### End

<table>
<tr>
<td width="40%">

By default, print will add a new line (`\n`) at the end of whatever it prints. If you wish to use a different character, you can set the `end` parameter.

</td>
<td width="60%">

```python
print('hello', end=' ')
print('world')
```
> hello world

</td>
</tr>
</table>



#### Multiple Parameters

<table>
<tr>
<td width="40%">

If you pass multiple arguments (separated by commas), it'll print them each on a single line with spaces in between. 

</td>
<td width="60%">

```python
name = 'Jane'
score = 97
print("Total score for", name, "is", score)
```
> Total score for Jane is 97

</td>
</tr>
</table>



#### Sep

<table>
<tr>
<td width="40%">

If you want to specify a different separator character (space is default), you can write something like:

</td>
<td width="60%">

```python
name = 'Jane'
score = 97
print("Total score for ", name, " is ", score, sep='_')
```
> Total_score_for_Jane_is_97

</td>
</tr>
</table>




### Input

<table>
<tr>
<td width="40%">

The `input` function allows us to prompt the user for input on the terminal. The string that's passed to it determines what's displayed with the prompt. [python docs](https://docs.python.org/3/library/functions.html#input)

</td>
<td width="60%">

```python
name = input('What is your name? ')
print('Hello', name, '!')

```
> What is your name? Joe<br>
> Hello Joe !

</td>
</tr>
</table>


## Terminal Fun

### ASCII Art

<table>
<tr>
<td width="40%">

You can make your terminal interface a bit more fun with ASCII art. The easiest way to add a multi-line string in Python is using a [docstring](Docstrings.md). Another good idea is to put all your ASCII art in a separate module so it doesn't clutter up your main file.

- [Library of ASCII art](https://www.asciiart.eu/)
- [Python module to generate ASCII art](https://pypi.org/project/art/)
  - Install with `pip install art`
  - Import it into your module `from art import *`
  - Call methods like `aprint("butterfly")`
- [Convert text to ASCII art](https://www.patorjk.com/software/taag/)

</td>
<td width="60%">

**art.py**
```python
border = '''
  .--.      .--.      .--.      .--.      .--.      .--.      .--.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\
'      `--'      `--'      `--'      `--'      `--'      `--'      `--'      `'''

owl = '''
 ,_,
(O,O)
(   )
-"-"-
'''
```

**main.py**
```python
import art
print(art.border)
print(art.owl)
```

</td>
</tr>
</table>

### Delayed Print

<table>
<tr>
<td width="40%">

You can use `time.sleep()` to add suspense to your messages.

</td>
<td width="60%">

```python
import random
print('Rolling dice...')
time.sleep(3)
print('You rolled a', random.randint(1,6))
```

</td>
</tr>
<tr>
<td width="40%">

You can also print things slowly.

</td>
<td width="60%">

```python
message = 'hello world!'
for char in message:
  print(char, end='', flush=True)
  time.sleep(.1)
    
```

</td>
</tr>
</table>

### Color

<table>
<tr>
<td width="40%">

[Colorama](https://pypi.org/project/colorama/) allows you to add color to your terminal output by printing special characters. Remember to reset colors if you want to don't want subsequent prints to also be in that color.

- Install colorama with `pip install colorama`
- Import the functions `from colorama import Fore, Back, Style`
- Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
- Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
- Style: DIM, NORMAL, BRIGHT, RESET_ALL

</td>
<td width="60%">

```python
from colorama import Fore, Back, Style
print(Fore.RED + 'this is red text')
print(Back.BLUE + 'this is red text on a blue background')
print(Style.RESET_ALL)
print('back to normal')
```

</div>