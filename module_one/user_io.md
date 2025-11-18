# User I/O

## The Console

The console is an application that lets us interact with a computer using text-based input. The console gives us 
more control over a computer and lets us do more advanced things. One of the many things consoles can do is run 
applications, and that's where the applications you create in this course will be run. Applications created for 
running in a console are called *console applications*. This doesn't mean that all applications don't use the 
console in some way. Applications can use the console to output messages reflecting things like progress on a 
particular task, for example, or to output errors.

### Console Output

If we want to send text from our applications to the console (or potentially some other location), we use the 
`print` function. The following code shows how to use the `print` function.

```python
print("Hello, world!")
print("It's nice to meet you!")
```

The above code outputs the following to the console.

```
Hello, world!
It's nice to meet you!
```

Notice how each print statement prints text on its own line? That's normally what we want, which is why Python does 
it by default. However, there are times when we'd like to print a bunch of things on the same line. The following 
code demonstrates how we can use the `end` keyword argument to do this.

```python
print("Hello, ", end="")
print("world!")
```

The above code outputs the following to the console.

```
Hello, world!
```

You can specify anything for the `end` argument. As an example, the following code always prints an ellipsis at the 
end of each output followed by a space. It definitely makes Python seem more thoughtful...

```python
print("Hello, world", end="... ")
print("It's a wonderful day today", end="... ")
print("I'm hungry", end="... ")
```

The above code outputs the following to the console.

```
Hello, world... It's a wonderful day today... I'm hungry...
```

#### Keyword Arguments

In Python, there are times when we need to pass arguments by name. This means including the name of the parameter 
when we pass the argument. `end=""` is an example of a keyword argument since we can't just pass `""` on its own. 
There are times when passing an argument as a keyword argument is required with failure to do so resulting in an 
error. Other times, it's done so for clarity rather than necessity. In the case of the `print` function, it's 
required, though you won't get an error if you forget `end=`, you'll simply get the default behavior for the `print` 
function.

#### `end` Parameter

The `end` parameter controls what's printed after the main content. The default value for this parameter is `"\n"` 
which is why `print` outputs a newline after each call. When we write something like `print("text", end="")`, we're 
overriding the newline that `print` would normally output after our text.

#### Newline Character

If we want to start text on a new line when printing, we can use the newline character. The *newline character* is a 
character that represents pressing the RETURN key on your keyboard when writing text. The newline character is 
written as `\n` in a string. The backslash is there to escape the `n` since `n` by itself is simply the letter n.

#### Escape Character

Backslashes serve a special purpose in strings. Backslash (`\`) is known as the *escape character* because it's job 
is to escape the default value or function of a character so it can be an alternate value or perform an alternate 
function. The following code demonstrates how we could use the escape character to print tabs, newlines, and double 
quotes in double-quoted strings.

```python
print("\t\"Hello, world!\" said Python.")
print("\t\"It's a great day today!\"")
print("You wondered how Python could understand the concept of a great day.")
print("\nYou weren't sure what to make of this...")
```

The above code outputs the following to the console.

```
    "Hello, world!" said Python.
    "It's a great day today!"
You wondered how Python could understand the concept of a great day.

You weren't sure what to make of this...
```

Since the escape character is special, what happens if we want to print a backslash? We simply escape the escape 
character!

```python
print("Here is a backslash: \\")
```

The above code outputs the following to the console.

```
Here is a backslash: \
```

### Console Input

We can also have our applications accept input from the console! This means we can ask a user for information so we 
can tailor the applications functionality to their needs. To ask the user for input in Python, we use the `input` 
function. The following code demonstrates asking the user for their name.

```python
name = input("Enter your name: ")
print(f"Nice to meet you, {name}!")
```

The above code outputs the following to the console. The name John on the first line was typed by the user.

```
Enter your name: John
Nice to meet you, John!
```

The `input` function accepts a prompt as an argument. This prompt is printed in the console, then the console will 
wait for the user to type something in and press RETURN to submit their input. The function will then return the 
text that was entered as a string.

Since we always get strings back from the `input` function, what if we want to ask the user for their age or their 
favorite number? We can use conversion functions like `int` and `float` to convert to different types!

```python
age = int(input("Enter your age: "))
fav_num = float(input("Enter your favorite number: "))
print(f"{age} is a great age!\nI like {fav_num}, too!")
```

The above code outputs the following to the console. The age 12 and the number 2.71 were typed by the user.

```
Enter your age: 12
Enter your favorite number: 2.71
12 is a great age!
I like 2.71, too!
```

Be aware that conversion functions like `int` and `float` will raise an error if it's not possible to convert the 
input string to the requested type. We will learn how to handle bad input later, so for now, assume your users 
always enter their input perfectly!
