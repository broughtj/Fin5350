
# Built-In Types: Simple Values

When discussing Python variables and objects, we mentioned the fact that all Python objects have type information attached. Here we'll briefly walk through the built-in simple types offered by Python.
We say "simple types" to contrast with several compound types, which will be discussed in the following section.

Python's simple types are summarized in the following table:

<center>**Python Scalar Types**</center>

| Type        | Example        | Description                                                  |
|-------------|----------------|--------------------------------------------------------------|
| ``int``     | ``x = 1``      | integers (i.e., whole numbers)                               |
| ``float``   | ``x = 1.0``    | floating-point numbers (i.e., real numbers)                  |
| ``complex`` | ``x = 1 + 2j`` | Complex numbers (i.e., numbers with real and imaginary part) |
| ``bool``    | ``x = True``   | Boolean: True/False values                                   |
| ``str``     | ``x = 'abc'``  | String: characters or text                                   |
| ``NoneType``| ``x = None``   | Special object indicating nulls                              |

We'll take a quick look at each of these in turn.

## Integers
The most basic numerical type is the integer.
Any number without a decimal point is an integer:


```python
x = 1
type(x)
```




    int



Python integers are actually quite a bit more sophisticated than integers in languages like ``C``.
C integers are fixed-precision, and usually overflow at some value (often near $2^{31}$ or $2^{63}$, depending on your system).
Python integers are variable-precision, so you can do computations that would overflow in other languages:


```python
2 ** 200
```




    1606938044258990275541962092341162602522202993782792835301376



Another convenient feature of Python integers is that by default, division up-casts to floating-point type:


```python
5 / 2
```




    2.5



Note that this upcasting is a feature of Python 3; in Python 2, like in many statically-typed languages such as C, integer division truncates any decimal and always returns an integer:
``` python
# Python 2 behavior
>>> 5 / 2
2
```
To recover this behavior in Python 3, you can use the floor-division operator:


```python
5 // 2
```




    2



Finally, note that although Python *2.x* had both an ``int`` and ``long`` type, Python 3 combines the behavior of these two into a single ``int`` type.

## Floating-Point Numbers
The floating-point type can store fractional numbers.
They can be defined either in standard decimal notation, or in exponential notation:


```python
x = 0.000005
y = 5e-6
print(x == y)
```

    True



```python
x = 1400000.00
y = 1.4e6
print(x == y)
```

    True


In the exponential notation, the ``e`` or ``E`` can be read "...times ten to the...",
so that ``1.4e6`` is interpreted as $~1.4 \times 10^6$.

An integer can be explicitly converted to a float with the ``float`` constructor:


```python
float(1)
```




    1.0



### Aside: Floating-point precision
One thing to be aware of with floating point arithmetic is that its precision is limited, which can cause equality tests to be unstable. For example:


```python
0.1 + 0.2 == 0.3
```




    False



Why is this the case? It turns out that it is not a behavior unique to Python, but is due to the fixed-precision format of the binary floating-point storage used by most, if not all, scientific computing platforms.
All programming languages using floating-point numbers store them in a fixed number of bits, and this leads some numbers to be represented only approximately.
We can see this by printing the three values to high precision:


```python
print("0.1 = {0:.17f}".format(0.1))
print("0.2 = {0:.17f}".format(0.2))
print("0.3 = {0:.17f}".format(0.3))
```

    0.1 = 0.10000000000000001
    0.2 = 0.20000000000000001
    0.3 = 0.29999999999999999


We're accustomed to thinking of numbers in decimal (base-10) notation, so that each fraction must be expressed as a sum of powers of 10:
$$
1 /8 = 1\cdot 10^{-1} + 2\cdot 10^{-2} + 5\cdot 10^{-3}
$$
In the familiar base-10 representation, we represent this in the familiar decimal expression: $0.125$.

Computers usually store values in binary notation, so that each number is expressed as a sum of powers of 2:
$$
1/8 = 0\cdot 2^{-1} + 0\cdot 2^{-2} + 1\cdot 2^{-3}
$$
In a base-2 representation, we can write this $0.001_2$, where the subscript 2 indicates binary notation.
The value $0.125 = 0.001_2$ happens to be one number which both binary and decimal notation can represent in a finite number of digits.

In the familiar base-10 representation of numbers, you are probably familiar with numbers that can't be expressed in a finite number of digits.
For example, dividing $1$ by $3$ gives, in standard decimal notation:
$$
1 / 3 = 0.333333333\cdots
$$
The 3s go on forever: that is, to truly represent this quotient, the number of required digits is infinite!

Similarly, there are numbers for which binary representations require an infinite number of digits.
For example:
$$
1 / 10 = 0.00011001100110011\cdots_2
$$
Just as decimal notation requires an infinite number of digits to perfectly represent $1/3$, binary notation requires an infinite number of digits to represent $1/10$.
Python internally truncates these representations at 52 bits beyond the first nonzero bit on most systems.

This rounding error for floating-point values is a necessary evil of working with floating-point numbers.
The best way to deal with it is to always keep in mind that floating-point arithmetic is approximate, and *never* rely on exact equality tests with floating-point values.

## Complex Numbers
Complex numbers are numbers with real and imaginary (floating-point) parts.
We've seen integers and real numbers before; we can use these to construct a complex number:


```python
complex(1, 2)
```




    (1+2j)



Alternatively, we can use the "``j``" suffix in expressions to indicate the imaginary part:


```python
1 + 2j
```




    (1+2j)



Complex numbers have a variety of interesting attributes and methods, which we'll briefly demonstrate here:


```python
c = 3 + 4j
```


```python
c.real  # real part
```




    3.0




```python
c.imag  # imaginary part
```




    4.0




```python
c.conjugate()  # complex conjugate
```




    (3-4j)




```python
abs(c)  # magnitude, i.e. sqrt(c.real ** 2 + c.imag ** 2)
```




    5.0



## String Type
Strings in Python are created with single or double quotes:


```python
message = "what do you like?"
response = 'spam'
```

Python has many extremely useful string functions and methods; here are a few of them:


```python
# length of string
len(response)
```




    4




```python
# Make upper-case. See also str.lower()
response.upper()
```




    'SPAM'




```python
# Capitalize. See also str.title()
message.capitalize()
```




    'What do you like?'




```python
# concatenation with +
message + response
```




    'what do you like?spam'




```python
# multiplication is multiple concatenation
5 * response
```




    'spamspamspamspamspam'




```python
# Access individual characters (zero-based indexing)
message[0]
```




    'w'



For more discussion of indexing in Python, see ["Lists"](06-Built-in-Data-Structures.ipynb#Lists).

## None Type
Python includes a special type, the ``NoneType``, which has only a single possible value: ``None``. For example:


```python
type(None)
```




    NoneType



You'll see ``None`` used in many places, but perhaps most commonly it is used as the default return value of a function.
For example, the ``print()`` function in Python 3 does not return anything, but we can still catch its value:


```python
return_value = print('abc')
```

    abc



```python
print(return_value)
```

    None


Likewise, any function in Python with no return value is, in reality, returning ``None``.

## Boolean Type
The Boolean type is a simple type with two possible values: ``True`` and ``False``, and is returned by comparison operators discussed previously:


```python
result = (4 < 5)
result
```




    True




```python
type(result)
```




    bool



Keep in mind that the Boolean values are case-sensitive: unlike some other languages, ``True`` and ``False`` must be capitalized!


```python
print(True, False)
```

    True False


Booleans can also be constructed using the ``bool()`` object constructor: values of any other type can be converted to Boolean via predictable rules.
For example, any numeric type is False if equal to zero, and True otherwise:


```python
bool(2014)
```




    True




```python
bool(0)
```




    False




```python
bool(3.1415)
```




    True



The Boolean conversion of ``None`` is always False:


```python
bool(None)
```




    False



For strings, ``bool(s)`` is False for empty strings and True otherwise:


```python
bool("")
```




    False




```python
bool("abc")
```




    True



For sequences, which we'll see in the next section, the Boolean representation is False for empty sequences and True for any other sequences


```python
bool([1, 2, 3])
```




    True




```python
bool([])
```




    False


