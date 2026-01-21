# More about Types

## Declaring More than One Type

Sometimes, we want to write functions that can return more than one data type. Sometimes, we want to declare 
variables that can hold more than one data type. We can do this by using a *type union*. The following code 
demonstrates writing a function which returns either an integer or a float depending on the value of the argument.

```python
def int_or_float(choice: str) -> int | float:
    return 7 if choice.casefold() == 'int' else 2.1
```

To create a type union, simply list the possible types separated by pipe characters (`|`). The following code 
demonstrates declaring a variable which can hold one of three possible types. We can ask Python for the type of a

```python
number: int | float | str = "five"
print(number)
```

You can create type unions with as many types as you want!

## Type Aliases

Sometimes, type unions can long. Other times, type unions might not give a good idea as to their purposes. We can 
solve both of these problems using *type aliases*. A type alias is a way to give another name to an existing type. 
We can use type aliases to name type unions to give a name to a set of different types. The following code 
demonstrates this.

```python
type Number = int | float | str
number: Number = 2.71
print(number)
```

Type aliases are one of the rare places where a keyword is used to declare something: we use the `type` keyword to 
define a type alias. We can then use that type alias in place of the aliased type. This can help make our code 
shorter and more readable!

When we create type aliases, we name them using *PascalCase* where the first letter of each word is capitalized, and 
no characters are used to join words. This is Python's preferred naming convention for data types.

## The `type` Function

If we want to get the data type of a value for display purposes, we can use the `type` function. The following code 
demonstrates using the `type` function.

```python
num = 57
print(type(num))
```

The above code outputs the following to the console.

```text
<class 'int'>
```

This can be helpful when debugging code involving multiple different types. This function should only be used when 
we want to display the type of a value. The following section demonstrates how we can check if a variable holds a 
particular type of value for logic purposes.

## The `isinstance` Function

If we want to check if a variable holds a certain type of value for logic purposes, we can use the `isinstance` 
function. The following code demonstrates how a function could check the data type of an argument.

```python
def print_num(num: int | float) -> None:
    print(f"{"Integer: " if isinstance(num, int) else "Float: "}{num}")


print_num(4)
```

The above code outputs the following to the console.

```text
Integer: 4
```

Anything that can be used as a type annotation can be used in an `isinstance` check. This includes type aliases!
