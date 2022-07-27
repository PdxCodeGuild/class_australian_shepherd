
# Numbers and Arithmetic


## Ints

<table>
<tr>
<td width="40%">

'Ints' represent integers, or 'whole numbers', and they can be positive or negative.

</td>
<td width="60%">

```python
x = 5
print(x) # 5
print(type(x)) # <class 'int'>
```

</td>
</tr>
</table>



## Floats

<table>
<tr>
<td width="40%">

'Float' is stort for 'floating-point number', which represents an approximation of a real number. Floats may also be written with an exponent, designated by `e`: `3.12e6` is 3,120,000.

</td>
<td width="60%">

```python
x = 5.23
print(x) # 5.23
print(type(x)) # <class 'float'>
```

</td>
</tr>
<tr>
<td width="40%">

There are also three special values floats may take: positive infinity, negative infinity, and NaN. NaN is short for 'not a number', it's the result of some mathematical operations, particularly in `numpy`. You can check for these values with the [math module](#the-math-module).

</td>
<td width="60%">

```python
import math

x = float('nan')
print(math.isnan(x)) # True

y = float('inf')
print(math.isinf(y)) # True

z = float('-inf')
print(math.isinf(z)) # True
print(math.isfinite(z)) # False
```

</td>
</tr>
</table>




## Arithmetic Operators

<table>
<tr>
<td width="40%">

### Addition: `a + b`, `a += b`

</td>
<td width="60%">

```python
print(5 + 2)
```

> 7

</td>
</tr>
<tr>
<td width="40%">

### Subtraction: `a - b`, `a -= b`

</td>
<td width="60%">

```python
print(5 - 2)
```

> 3

</td>
</tr>
<tr>
<td width="40%">

### Multiplication: `a * b`, `a *= b`

</td>
<td width="60%">

```python
print(5 * 2)
```

> 10

</td>
</tr>
<tr>
<td width="40%">

### Division: `a / b`, `a /= b`

</td>
<td width="60%">

```python
print(5 / 2)
```

> 2.5

</td>
</tr>
<tr>
<td width="40%">

### Floor Division: `a // b`, `a //= b`

Floor division is like regular division, but the result is rounded down to the nearest integer.

</td>
<td width="60%">

```python
print(5 // 2)
```

> 2

</td>
</tr>
<tr>
<td width="40%">

### Modulus: `a % b`, `a %= b`

Modulus is the 'remainder function' for example, `a%b` is the remainder of `a/b`.


</td>
<td width="60%">

```python
print(5 % 2)
print(99 % 3)
```

> 1
> 0

</td>
</tr>
<tr>
<td width="40%">

Modulus also useful for containing the range of a variable.


</td>
<td width="60%">

```python
i = 0
while i < 100:
    print(i%3, end=' ')
    i = i + 1
```
> 0 1 2 0 1 2 0 1 2 ...

</td>
</tr>
<tr>
<td width="40%">

### Exponentiation: `a ** b`, `a **= b`

</td>
<td width="60%">

```python
print(5 ** 2)
```

> 25

</td>
</tr>
</table>

## Built-in Functions

<table>
<tr>
<td width="40%">

### Type Conversions

</td>
<td width="60%">

```python
# convert a string to an int
print(int('5')) # 5
# convert a float to an int
print(int(5.23)) # 5
# convert a 
print(float('5.0')) # 5.0
```

</td>
</tr>
<tr>
<td width="40%">

### Absolute Value `abs(x)`

</td>
<td width="60%">

```python
print(abs(5)) # 5
print(abs(-2)) # 2
```

</td>
</tr>
<tr>
<td width="40%">

### Round `round(x)`

</td>
<td width="60%">

```python
print(round(5.2)) # 5
print(round(2.6)) # 3
```

</td>
</tr>
<tr>
<td width="40%">

### Minimum `min(x)`

</td>
<td width="60%">

```python
print(min(5, 2)) # 2
```

</td>
</tr>
<tr>
<td width="40%">

### Maximum `max(x)`

</td>
<td width="60%">

```python
print(max(5, 2)) # 5
```

</td>
</tr>
<tr>
<td width="40%">

### Sum `sum(x)`

</td>
<td width="60%">

```python
print(sum(5, 2, 3)) # 10
```

</td>
</tr>
</table>

## The Math Module

The `math` module has many specialized math functions you can utilize, a full list of them can be found [here](https://docs.python.org/3/library/math.html).

<table>
<tr>
<td width="40%">

### Floor `math.floor(x)`

</td>
<td width="60%">

```python
import math
print(math.floor(5.5)) # 5
```

</td>
</tr>
<tr>
<td width="40%">

### Ceiling `math.ceil(x)`

</td>
<td width="60%">

```python
import math
print(math.ceil(5.5)) # 6
```

</td>
</tr>
<tr>
<td width="40%">

### Square-root `math.sqrt(x)`

</td>
<td width="60%">

```python
import math
print(math.floor(9)) # 3
```

</td>
</tr>
<tr>
<td width="40%">

### Pi `math.pi`


</td>
<td width="60%">

```python
import math
print(math.pi) # 3.1415963...
```

</td>
</tr>
<tr>
<td width="40%">

### Cosine `math.cos(x)`

</td>
<td width="60%">

```python
import math
print(math.cos(math.pi/2)) # 0
```

</td>
</tr>
<tr>
<td width="40%">

### Sine `math.sin(x)`

</td>
<td width="60%">

```python
import math
print(math.sin(math.pi/2)) # 1
```

</td>
</tr>
</table>

