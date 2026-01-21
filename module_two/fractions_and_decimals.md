# Additional Numeric Types

## Issues with Floating-point Numbers

Python has two basic numeric data types, `int` and `float`. Integers are infinitely precise and can be as big as we 
want. Floats, on the other hand, can only occupy a certain size, and they have precision issues. One way we can see 
the precision issues with floating-point numbers is by running the following code.

```python
print(0.1 + 0.2)
```

The above code outputs the following to the console.

```text
0.30000000000000004
```

That's not quite the 0.3 we were expecting. This happens because floating-point numbers are stored in binary. There 
are rational and irrational numbers in decimal which can't be completely represented because they are infinitely 
repeating. Numbers like $\frac{1}{3}$, $e$, and $pi$ can't be accurately represented. Numbers like these also exist in binary, 
too, and we can run into issues when floating-point numbers are converted to binary. Numbers like 0.1 and 0.2 become 
infinitely repeating when converted to binary, which means their fractional part will need to be limited to a 
certain number of digits. This causes some imprecision which is compounded when math is performed.

This normally isn't a big deal because binary floating-point numbers are the fastest kind of floating-point number. 
If we don't need to be super precise, this level of imprecision is so small that it's negligible. However, what if 
we wanted to store a bank balance? We would need a data type that wouldn't lose precision simply because it's used 
in some equations. What if we need to represent values like $\frac{1}{3}$ as accurately as possible? This is where 
Python's other numeric data types come in!

## The `Decimal` Type

If we need to represent a floating-point number with infinite accuracy up to a certain number of decimal places, we 
can use Python's `Decimal` type. This type stores floating-point numbers in decimal instead of binary, so they're 
infinitely accurate like integers! The following code demonstrates how to create a `Decimal` value and how to do 
some basic arithmetic.

```python
from decimal import Decimal

num_1 = Decimal('0.1')
num_2 = Decimal('0.2')
print(num_1 + num_2)
```

The above code outputs the following to the console.

```text
0.3
```

First, we see that we need to import the `Decimal` type from the `decimal` module. Second, we see that we use the 
`Decimal` function to create a decimal value. Third, we see that we need to provide the decimal value as a string. 
Let's see what happens if we don't provide it as a string.

```python
print(Decimal(0.1))
```

The above code outputs the following to the console.

```text
0.1000000000000000055511151231257827021181583404541015625
```

Since 0.1 is a float, it gets converted to binary, which means it's already been approximated before a decimal is 
created from it. We can actually see the inaccuracy in 0.1 that we normally can't see when we do this! This is why 
we need to provide decimal values as strings: no accuracy is lost since strings aren't numeric types!

Math between `Decimal` objects is supported, but let's see what happens if we try printing the sum of a decimal and 
a regular float.

```python
print(Decimal('0.1') + 0.2)
```

The above code outputs the following to the console.

```text
main.py:3: error: Unsupported operand types for + ("Decimal" and "float")  [operator]
Found 1 error in 1 file (checked 1 source file)
```

`mypy` gives us an error because this is not supported. It makes sense since we probably don't want to be using 
regular floats if we're bothering to use the `Decimal` type. Trying this with a decimal and an integer, however, works.

```python
print(Decimal('0.1') + 1)
```

The above code outputs the following to the console.

```text
1.1
```

The above code yields another `Decimal` object. Since integers and decimals are both infinitely accurate, there's no 
issue here!

What happens if we try to create a `Decimal` object with a non-number?

```python
print(Decimal('apple'))
```

The above code outputs the following to the console.

```text
Traceback (most recent call last):
  File "/project/src/main.py", line 3, in <module>
    print(Decimal('apple'))
          ~~~~~~~^^^^^^^^^
decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
```

We get an `InvalidOperation` error in response. Frustratingly, we don't get a `ValueError` which would make more 
sense given the behavior of Python's other numeric types when supplied bad values. Since this error is 
decimal-specific, we need to import it when we import the `Decimal` type if we want to check for it in a 
try-except-block.

Additionally, decimals are accurate to 28 digits by default, but that can be changed if needed. We'll never need to 
change it, so we won't worry about it.

## The `Fraction` Type

If we need to store a rational number accurately, we can use the `Fraction` type! The following code demonstrates 
storing a rational number.

```python
from fractions import Fraction

frac = Fraction('1/3')
print(frac)
```

The above code outputs the following to the console.

```text
1/3
```

The `Fraction` type is imported from the `fractions` module. We can then create a `Fraction` object using the 
`Fraction` function and providing it the fraction as a string. It's also possible so supply the numerator and 
denominator separately if needed, though this should only be done if the numerator and denominator are already separate.

```python
frac = Fraction(1, 3)
print(frac)
```

We can perform basic arithmetic with fractions.

```python
print(Fraction('1/3') + Fraction('4/5'))
```

The above code outputs the following to the console.

```text
17/15
```

Fractions automatically figure out how to add themselves, and they give you the most simplified fraction as a result.

Fractions can also be added to both integers and floats.

```python
print(Fraction('1/3') + 7)
print(Fraction('4/5') + 0.27)
```

The above code outputs the following to the console.

```text
22/3
1.07
```

Make sure to be careful of this if you need an accurate decimal. So, what if we need to add a `Fraction` object and 
a `Decimal` object?

```python
print(Fraction('1/3') + Decimal('0.3'))
```

The above code outputs the following to the console.

```text
main.py:4: error: No overload variant of "__add__" of "Fraction" matches argument type "Decimal"  [operator]
main.py:4: note: Possible overload variants:
main.py:4: note:     def __add__(a, int | Fraction, /) -> Fraction
main.py:4: note:     def __add__(a, float, /) -> float
main.py:4: note:     def __add__(a, complex, /) -> complex
Found 1 error in 1 file (checked 1 source file)
```

`mypy` tells us that there is no way to add a fraction and a decimal. This is because Python can't be sure if we 
want to approximate the fraction as a decimal, or if we want to represent the decimal as a fraction. This means we 
need to convert one type to the other, which we'll learn in the next section.

## Converting between `Decimal` and `Fraction`

We can convert a decimal to a fraction super easily.

```python
frac = Fraction('1/3')
dec = Decimal('0.3')
print(frac + Fraction(dec))
```

The above code outputs the following to the console.

```text
19/30
```

We can simply use the `Fraction` function to convert from a decimal to a fraction.

On the other hand, converting a Fraction to a decimal is not as easy.

```python
frac = Fraction('1/3')
dec = Decimal('0.3')
print(Decimal(frac) + dec)
```

The above code outputs the following to the console.

```text
main.py:40: error: Argument 1 to "Decimal" has incompatible type "Fraction"; expected "Decimal | float | str | tuple[int, Sequence[int], int]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

This is because Python can't be sure if we're okay with approximations when the conversion takes place. We can 
perform this convertion ourselves by simply converting the numerator and denominator to decimals, then dividing them.

```python
frac = Fraction('1/3')
dec = Decimal('0.3')
print(Decimal(frac.numerator) / Decimal(frac.denominator) + dec)
```

The above code outputs the following to the console.

```text
0.6333333333333333333333333333
```
