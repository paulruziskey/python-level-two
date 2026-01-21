# Error Handling

Errors are a fundamental aspect of programming, and they come in different forms. The form you're most familiar with is 
*syntax error*. Syntax errors are raised when we violate Python's syntax rules, and these errors prevent our code from 
compiling.

Another form of error is *runtime error*. You've most likely experienced this error form when getting user input. 
Conversion functions like `int` and `float` will raise runtime errors if it's not possible to convert a string to the 
desired type. These errors are a bit different from syntax errors since they don't prevent our code from compiling, 
they only crash our programs once they're raised.

Runtime errors typically signal bugs in our program. This means we usually write code to avoid runtime errors being 
thrown. For example, if we ask a user for two numbers so we can compute their quotient, we would need to write code to 
prevent the user from entering zero as the divisor. Otherwise, our code would raise a `ZeroDivisionError` as soon as it 
tried to divide anything by zero.

Sometimes, however, runtime errors signal an erroneous situation outside the programmer's control. For example, asking 
a user for an integer, but they enter a word. We can't write code that checks for that in the user's input string 
before attempting to convert it to an integer. This is where *error handling* comes in!

## What Is Error Handling?

Error handling is when we write code that handles particular runtime errors so they don't crash our program. The main 
reason runtime errors crash our programs is because Python doesn't know what to do when they happen. Errors represent 
exceptional situations that would lead to issues if they were allowed to continue, but if we know how to deal with
these exceptional situations, then we can write code that handles them!

## Try-except-blocks

### Basic Usage

We handle errors in Python using *try-except-blocks*. These blocks follow similar logic to if-blocks. Try-except-blocks 
start with a try-statement which contains code that could potentially raise an error. If the code in the try-statement 
runs without raising any errors, the rest of the try-except block is skipped. If an error is raised at any point in the 
try-statement, the statement is exited immediately, and Python looks for an except-clause which handles the 
particular error that was raised. The following code demonstrates handling the `ValueError` that can be raised from the 
`int` function if an attempt is made to convert a non-integer to an integer.

```python
try:
    num = int(input("Enter an integer: "))
    print(f"You entered: {num}")
except ValueError:
    print("You didn't enter a valid integer")

try:
    num_2 = int(input("Enter another integer: "))
    print(f"You entered: {num_2}")
except ValueError:
    print("You didn't enter a valid integer")
```

The above code outputs the following to the console.

```text
Enter an integer: 3
You entered: 3
Enter another integer: apple
You didn't enter a valid integer
```

Notice how the print statement in the second try-except-block doesn't run because an error was raised by the `int` 
function? This is important to recognize because it affects how we write code around try-except-blocks. Something else 
that's important to note is that all errors in Python are simply instances of particular data types! In the above 
example, `ValueError` is the data type of the raised error. This means except-clauses are written to handle particular 
types of errors. It's also important to note that, unlike if-statements, try-statements *cannot* be written by 
themselves. Try-statements require at least one of two types of additional clauses to be syntactically valid, one of 
which is the except-clause. We will learn about the other type of clause in a later section.

It's possible to handle more than one possible error from a block of code. The following code demonstrates handling 
both a `ValueError` and a `ZeroDivisionError`.

```python
try:
    divisor = int(input("Enter a number to divide three by: "))
    print(f"3 / {divisor} = {3 // divisor}")
except ValueError:
    print("You didn't enter a valid integer")
except ZeroDivisionError:
    print("Can't divide by zero")
```

The above code outputs the following to the console.

```text
Enter a number to divide three by: 0
Can't divide by zero
```

For the sake of this example, a `ZeroDivisionError` is being handled by a try-except-block, but in general, they should 
be handled by simply making sure they aren't raised in the first place. It's important to recognize when an error is 
being raised due to a bug versus being raised due to user error.

When multiple except-clauses are present, they are checked in the order they are written, and whichever one is matched 
first is the one that's executed. Python's errors are part of a hierarchy, meaning errors are built on each other. When 
handling separate errors like the above errors, the order of except-clauses doesn't matter, but when handling a 
specific error and a more generic error, the more generic error should go last. We'll see an example of this behavior 
in the next section.

### Handling Multiple Errors

Sometimes we need to handle multiple errors, but we want to do the same thing for each error. The following code 
demonstrates how we can handle multiple errors using the same except-clause by simply listing the error types separated
by commas.

```python
try:
    divisor = int(input("Enter a number to divide three by: "))
    print(f"3 / {divisor} = {3 // divisor}")
except ValueError, ZeroDivisionError:
    print("Bad input")
```

The above code outputs the following to the console.

```text
Enter a number to divide three by: 0
Bad input
```

We can see that there's actually a loss of clarity in doing so depending on the situation. In general, it's better to 
handle errors separately if it increases the clarity of the situation. That being said, there are times when multiple 
errors all need to be handled in the same way, so it's up to you to figure out the best way to write your code.

### Error Objects

Earlier, we discovered that errors are actually instances of error types. This means there's an actual object being 
passed around when an error is raised. In the previous examples, we didn't care about the details of the error objects 
being raised; we simply wanted to handle particular types of errors if they happened. However, there are times when 
having the raised object is helpful. For example, we can get the error message from an error object. The following code 
demonstrates this.

```python
try:
    divisor = int(input("Enter a number to divide three by: "))
    print(f"3 / {divisor} = {3 // divisor}")
except ValueError as ex:
    print(f"Bad input: {ex}")
except ZeroDivisionError:
    print(f"Can't divide by zero")
```

The above code outputs the following to the console.

```text
Enter a number to divide three by: apple
Bad input: invalid literal for int() with base 10: 'apple'
```

Simply converting an error object to a string (which happens automatically in f-strings) yields the error message! This 
can be quite helpful when we merely want to print what went wrong when an error occurs since we can handle all errors 
with a single except-clause. The code below demonstrates this.

```python
try:
    divisor = int(input("Enter a number to divide three by: "))
    print(f"3 / {divisor} = {3 // divisor}")
except (ValueError, ZeroDivisionError) as ex:
    print(f"Bad input: {ex}")
```

The above code outputs the following to the console.

```text
Enter a number to divide three by: 0
Bad input: division by zero
```

Note that we have to add parentheses around the list of error types when we wish to capture the error object.

Handling many errors with a single except-clause can be quite convenient, but we have to be careful: Python error 
messages usually aren't readable to non-programmers. Imagine if your parent/guardian or your grandparent had to read 
it; would they understand what they did wrong in as unambiguous a way as possible? With this in mind, it's often better 
to handle errors separately if it means your program outputs messages that are more readable.

### The General Except-clause

It's possible to write except-clauses that handle all types of errors. This is because Python data types are built from 
other data types. For error types, they are all based on Python's `Exception` type. The following code demonstrates 
handling all errors with the `Exception` type.

```python
try:
    num = int(input("Enter an integer: "))
except Exception as ex:
    print(f"No more crashing, but the following error occurred: {ex}")
```

The above code outputs the following to the console.

```text
Enter an integer: apple
No more crashing, but the following error occurred: invalid literal for int() with base 10: 'apple'
```

This is a bit dangerous because any errors that are raised in the try-statement will be handled by the except-clause. 
This means that errors we might not have thought about could be handled without us realizing! For this reason, we only 
want to handle the most specific kinds of errors we can. There are times, however, when we want to do something before 
an error crashes our program. That is when the general except-clause is used. This is typically done for logging 
purposes. The best practice is to make sure that general except-clauses return the program to a known-good state, or 
that they re-raise the raised error. The following code demonstrates the use of the `raise` keyword to re-raise the 
raised error in an except-clause.

```python
try:
    num = int(input("Enter an integer: "))
    print(f"3 // {num} = {3 // num}")
except ValueError:
    print("Bad input")
except Exception as ex:
    print(f"The following error occurred: {ex}")
    raise
```

The above code outputs the following to the console.

```text
Enter an integer: 0
The following error occurred: division by zero
Traceback (most recent call last):
  File "/project/src/main.py", line 40, in <module>
    print(f"3 // {num} = {3 // num}")
                          ~~^^~~~~
ZeroDivisionError: division by zero
```

It's important that the general except-clause go last since the except-clauses are checked in the order they're 
declared. Since the general except-clause handles all errors, any more specific clauses that come after it won't run!

### The Bare Except-clause

It's possible to write a bare except-clause in Python. The bare except-clause is an except-clause without an error type 
declared. The following code demonstrates this.

```python
try:
    num = int(input("Enter an integer: "))
except:
    print("I handle anything")
```

This clause handles even more than the general except-clause, which is why it should ***never be used***. If you use 
one in your code, most IDEs will issue a warning advising you to avoid using the bare except-clause. This section is 
purely for information purposes.

### The Else-clause

The else-clause of a try-statement is run when the try-statement ends naturally. In other words, the else-clause runs 
when the try-statement doesn't end early. Things like return-statements, break-statements, continue-statements, and 
errors being raised are all things that end a try-statement early. This means the else-clause can be used to run code 
if no errors are raised, but we have to keep in mind that it won't be run in every case when an error isn't raised. 
This means that else-statements aren't used that often, but it's good to know that they exist in case you see other 
code using them or in case they fit your use case. The following code demonstrates the use of an else-clause.

```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("You entered something else...")
else:
    print("You entered an integer!")
```

The above code outputs the following to the console in different cases.

```text
Enter an integer: 5
You entered an integer!
```

```text
Enter an integer: apple
You entered something else...
```

An else-clause can only be added to a try-statement when at least one except-clause is present, and the else-clause 
must appear after all except-clauses.

The following code demonstrates a return-statement ending a try-statement early.

```python
def get_integer() -> None:
    try:
        num = int(input("Enter an integer: "))
        if num == 7:
            print("You entered my favorite number!")
            return
    except ValueError:
        print("You entered something else...")
    else:
        print("You entered an integer!")


get_integer()
```

The above code outputs the following to the console in different cases.

```text
Enter an integer: 7
You entered my favorite number!
```

```text
Enter an integer: 8
You entered an integer!
```

We can see the else clause doesn't run when seven is entered since the try-statement ends via the return-statement 
instead of ending naturally.

### The Finally-clause

The finally-clause of a try-statement is run after the try-statement is exited. Unlike with the else-clause, the 
finally-clause will run no matter how a try-statement is exited. This is because finally-statements are for running 
what we call *cleanup code*. Cleanup code is code that finishes something that was started somewhere else. As of now, 
you don't know of any code that requires cleanup, but we'll still learn about the finally-clause so you'll be familiar 
with it when we get there. The following code demonstrates the use of a finally-clause.

```python
try:
    num = int(input("Enter an integer: "))
finally:
    print("Done getting input")
```

The above code outputs the following to the console in different cases.

```text
Enter an integer: 5
Done getting input
```

```text
Enter an integer: apple
Done getting input
Traceback (most recent call last):
  File "/project/src/main.py", line 2, in <module>
    num = int(input("Enter an integer: "))
ValueError: invalid literal for int() with base 10: 'apple'
```

Try-statements can be written with only a finally-clause. This may seem strange considering try-except-blocks are 
normally used to handle errors to prevent them from crashing our programs, but there are some cases where we have 
cleanup code to run that needs to run even if an error is raised. Notice how the finally-clause still runs in the case 
when an error is raised? Try-finally blocks were quite common in Python code prior to version 2.5 when Python added a 
better way to ensure cleanup code would run in the event of an error, so they're not used anymore, but it's good to 
know what Python does behind the scenes. We'll remind ourselves of this construction when we learn about code that 
requires cleanup.

Finally-clauses are typically used with other clauses. The following code demonstrates writing a try-except block with 
all three types of additional clauses. Finally-clauses are required to be the final clause of a try-statement when they 
are present.

```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("You entered something else...")
else:
    print("You entered an integer")
finally:
    print("Done getting input")
```

The above code outputs the following to the console in different situations.

```text
Enter an integer: 5
You entered an integer
Done getting input
```

```text
Enter an integer: apple
You entered something else...
Done getting input
```

## Suppressing Errors

### Typical Construction

While errors aren't fun to get, they're very helpful because they tell us exactly what went wrong and where it 
happened. Sometimes they can be a little cryptic, but they're still helpful. In Python, errors represent bugs in our 
code 95 percent of the time, and our job is to rewrite our code to prevent them from being raised. The other five 
percent of the time, however, they signal an event, and thus require no handling.

One such event may be Python's failure to convert an input to a specific type. For example, Python fails to convert 
floating-point numbers to integers. What if we wanted to accept both integers and floating-point numbers from a user, 
but we wanted them to be their proper types. In other words, it wouldn't be good enough for integers to be stored as 
floats. We could write the following code to achieve this.

```python
user_input = input("Enter a number: ")
try:
    user_num: int | float = int(user_input)
    print("Got an integer")
except ValueError:
    try:
        user_num = float(user_input)
        print("Got a float")
    except ValueError:
        print("Invalid number")
```

The above code outputs the following to the console in different situations.

```text
Enter a number: 4
Got an integer
```

```text
Enter a number: 2.1
Got a float
```

```text
Enter a number: apple
Invalid number
```

Firstly, `user_num` needs its type specified since floats are not assignable to integer variables. Secondly, we can see 
that the code is a little long for what it is, and it's not immediately clear that the `ValueError` from the `int` 
function is being ignored to try converting `user_input` to a float. Additionally, we like to avoid indenting code when 
we can, especially when it's part of the main code. We can, therefore, rewrite the code a bit using the `pass` keyword.

```python
def get_number() -> int | float | None:
    user_input = input("Enter a number: ")
    try:
        return int(user_input)
    except ValueError:
        pass
    try:
        return float(user_input)
    except ValueError:
        print("Invalid number")
    return None


user_num = get_number()
```

This code has the same behavior, but it's clear that the `ValueError` is being ignored since blocks with the `pass` 
keyword are intentionally left empty. Since the second try-except-block was no longer nested in the first 
except-clause, the code needed to be put inside a function so the second try-except-block wouldn't run if the integer 
conversion was successful. This is still a lot of code for what it is. This is where Python's with-statement can help!

### With-statements

With-statements are a way to apply a context to a block of code. We won't fully learn about them now, but we'll learn 
about how they can be used to suppress errors. In the above code, we wanted to suppress the `ValueError` from the `int` 
function since it meant that the code should attempt a float conversion instead. We can do this with a with-statement 
and the `contextlib.suppress` function.

```python
import contextlib


def get_number() -> int | float | None:
    user_input = input("Enter a number: ")
    with contextlib.suppress(ValueError):
        return int(user_input)
    try:
        return float(user_input)
    except ValueError:
        print("Invalid number")
    return None


user_num = get_number()
```

The above code works the same way as it did before, but this time, we didn't need the try-except-block. The 
with-statement is applying a context to its code block where `ValueError` is suppressed. If a `ValueError` is raised 
within this context, block will simply be exited, but other raised errors will still cause the program to crash. If an 
error needs to be suppressed, this is how it should be done.
