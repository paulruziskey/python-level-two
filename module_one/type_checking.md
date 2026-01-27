# Type Checking

## Dynamic Typing

### What Is Dynamic Typing?

Python is a *dynamically-typed* language. This means that variables can store values of whatever data types we need, 
and they can change at any time. The following code demonstrates dynamic typing.

```python
num = 1
print(num)
num = "one"
print(num)
```

The above code outputs the following to the console.

```text
1
one
```

### Consequences of Dynamic Typing

While this certainly makes typing code easier, and while this means we can write code more quickly, this is a bit of 
a problem when it comes to writing safe code. This is because certain data types can do certain things while others 
can't necessarily do those things, so data types aren't necessarily interchangeable. Python doesn't check types 
until it's time to do something with a value. If we try to do something we can't do with a value, Python will raise a 
`TypeError`.

```python
word = 3
print(word[0])  # TypeError because integers don't support the subscript operator
```

We can also have problems when data types *are* interchangeable because the outcome may not be what we expect, 
meaning we might have to spend awhile searching for a subtle bug that's not giving us any errors.

```python
def add(a, b):
    return a + b


print(add(1, 2))
print(add("hello", "world"))
```

The above code outputs the following to the console.

```text
3
helloworld
```

In the case of the above code, it may actually be a feature that the `add` function supports both integers and 
strings. In other cases, however, the same thing might happen, and it might be a bug instead of a feature.

### Why Dynamic Typing?

Dynamic typing generally makes it easier to write code since you don't have to worry about specifying data types 
everywhere. This generally makes it a popular choice for scripting languages where the main use case is writing 
short snippets of code which are easy to reason about since the code for each script may fit entirely on one page. 
For languages that involve more code, it makes things much more difficult since knowing what data types are required 
by pieces of code is important.

Python was originally designed as a prototyping language: it was designed for people to create proofs-of-concept. 
They would then implement the idea in another language once they'd figured out the details. Python has now been the 
most popular programming language in the world for several years due to its wide range of libraries for data science 
and machine learning as well as how easy it is to learn. Python was never intended for being used in production for 
serious projects, but here it is, so is there anything we can do about Python's dynamic typing?

## Static Typing in Python

### Type Annotations

*Static typing*, in contrast to dynamic typing, is when variables have specific data types associated with them 
which cannot be changed after being declared. The word *static* in this context means *fixed*, as opposed to 
*dynamic* meaning *changing*.

As of Python 3.5, we can include *type annotations* in our code! Type annotations give us a way to annotate the data 
types of variables and parameters as well as function return values. The following code shows the same code from 
earlier with type annotations. Variables are annotated by adding colons after their names and specifying their data 
types. Function return types are annotated by using an arrow formed from a hyphen and a closing angle bracket and 
specifying the type.

```python
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
print(add("hello", "world"))
```

The above code outputs the following to the console.

```text
3
helloworld
```

Is this surprising? Shouldn't we get an error because the `add` function clearly accepts integers and returns an 
integer? We might expect this, but type annotations are ignored when Python runs code. This is for several reasons.

1. Python tries to be as backwards-compatible as possible, meaning enforcing type annotations would be a *breaking 
   change*. A lot of code would have to be rewritten if people wanted to upgrade to a newer version of Python.
2. Python remains a *dynamically typed* language despite looking statically typed when annotations are present. The 
   entire language would have to be fundamentally overhauled to make Python actually statically typed which would 
   make Python into an entirely different language since Python was designed around dynamic typing.
3. Dynamic typing is useful for prototyping which was Python's original purpose, so it doesn't necessarily make 
   sense to remove Python's dynamic-typing abilities.

While adding type annotations doesn't cause Python to raise errors on type mismatches, many IDEs run static-analysis 
tools which report type mismatches. PyCharm has a good one built in, and it would emit the warning *Expected type 
'int', got 'str' instead* in for the above code. This means adding type annotations will cause type mismatches to 
become visible when they were previously invisible.

We also don't need to annotate every variable for this to work! We really only need to annotate function parameters 
and return types as well as types that contain other types (e.g., lists). Static-analysis tools can infer all other 
data types from these few annotated types!

One other bonus of adding type annotations is that it can help IDEs like PyCharm offer code completions that make 
sense. If PyCharm knows a particular function parameter is a string, it can offer string methods when offering 
autocompletion options!

#### Writing Basic Type Annotations

All data types can be used as type annotations. This includes the following list of types we've interacted with so far.

* `bool`
* `int`
* `float`
* `str`
* `list`
* `Turtle`

Let's say we need to annotate a function that takes in an integer and a boolean and returns a string. That would look 
like the following.

```python
def foo(num: int, is_something: bool) -> str:
   ...
```

All of the above data types are used like this when they are part of a type annotation except for `list` which is a bit 
more complicated. Since lists store values of a particular data type, we need to annotate that inner type as well. We 
do this by putting the inner type in square brackets after the `list` type, and we do this for all types which store an 
instance or instances of another type. Let's say we need to annotate a function that returns a list of integers. That 
would look like the following.

```python
def bar() -> list[int]:
   ...
```

As we learned in **Python Level One**, all functions return something. If we don't explicitly return something from a 
function, it will automatically return `None`. This means that functions that effectively return "nothing" are 
returning `None`. How do we annotate this? We can use `None` as an annotation, too! The following code shows type 
annotations on a function that doesn't return anything meaningful.

```python
def baz() -> None:
   ...
```

`None` is actually a special case since we can't do this with other values in the same way. For example, the following 
type annotations are invalid.

```python
def bad_annotations(always_true: True) -> 0:
   ...
```

Unfortunately, as discussed earlier, Python won't care if type annotations are invalid since it ignores them when 
running code. Luckily for us, there is a way to get errors when type mismatches come up in our code! The next section 
details how.

### Third-party Static-analysis Tools

Although the type-mismatch warnings we get after annotating types are much better than getting no indications that 
something is wrong in our code, our code can still be run with these possible bugs if we don't catch the warnings. 
That's where third-party static-analysis tools come in! These tools are external tools that can be run before our 
code is run to give us type errors that will prevent our code from running! They will also point to specific 
locations where these type errors occur so we can deal with them.

There are several tools that have been written for this task. We will be using a tool called `mypy`, and we will 
configure PyCharm to automatically run it before running our code! `mypy` is installed on a per-project basis, so if 
you just want to create a project for trying something out, you don't need to worry about it checking things you 
don't care about.

#### Installing `mypy` for a Project

To install `mypy` for a Python project open in PyCharm, first open the integrated terminal by clicking the icon at 
the bottom left.

![PyCharm terminal location](../../assets/images/level_two/module_one/pycharm_terminal_loc.jpg)

This can also be done by opening your computer's terminal and changing the directory to your project's directory.

Once the terminal is open, simply type the following and press RETURN

```text
pip install mypy
```

`pip` is Python's package manager. It manages third-party dependencies for your Python projects. It has been known 
to stand for a few things, but the most common thing PIP stands for is *PIP Installs Packages*. PIP is an acronym 
which references itself.

#### Configuring a Project to Run `mypy`

Now that `mypy` is installed, we need to configure our project so PyCharm runs `mypy` before our code whenever we 
run our code.

Click on the vertical ellipsis near the run button, then select the `Run with Parameters...` option.

![Creating project configuration](../../assets/images/level_two/module_one/config_dropdown.png)

A popup will come up with a bunch of information already filled out. All we need to do is add `mypy` as a 
before-launch task.

Click on the `Modify options` dropdown, then select `Add before launch task`.

![Add before-launch task](../../assets/images/level_two/module_one/add_before_launch_task.png)

Another popup will come up. Select `Run External Tool`.

![Run external tool](../../assets/images/level_two/module_one/run_external_tool.png)

This will open another popup. Which says that no external tools have been configured. Click the `+` icon at the top 
of the popup.

![Add new external tool](../../assets/images/level_two/module_one/add_external_tool.png)

A popup will open where we can enter information to create an external-tool configuration. First, enter "mypy" in the 
`Name` field. We now need to add information to the fields in the `Tool Settings` section. Luckily, PyCharm has 
predefined *macros* which are like variables that hold the correct information for the current project. Click the 
`+` icon at the right of the `Program` field.

![Inserting macro](../../assets/images/level_two/module_one/insert_macro.png)

Scroll through the options and double-click on the `PyInterpreterDirectory` macro. This will insert it into the 
`Program` field with dollar signs around it. You should then add "/mypy" after the last dollar sign. This field 
tells PyCharm what the external tool is that we want to run. The `PyInterpreterDirectory` macro actually points to 
the `bin` directory inside the `.venv` directory where PIP installs Python packages. We're simply selecting `mypy` 
from the directory that contains the installed Python packages for the current project. The `PyInterpreterDirectory` 
macro not only makes it so we don't have to manually enter the right path, it also makes it so we can use this same 
configuration in future projects without having to change anything!

Next comes the `Arguments` field. This field provides arguments to the external tool. `mypy` needs to know which 
file we want to check types for, so we enter "main.py" in this field.

Lastly, we need to specify a value for the `Working directory` field. This specifies where `mypy` is allowed to put 
files if it needs to. For this, select the `+` icon to add the `Projectpath` macro. The following image shows the 
configuration with everything entered properly.

![Final mypy config](../../assets/images/level_two/module_one/mypy_config.png)

Click the `OK` button to add the configuration for `mypy`. Now we need to select it and add it to the project by 
highlighting it in the tools popup and clicking `OK`.

![Selecting mypy](../../assets/images/level_two/module_one/select_mypy.png)

You should now see `mypy` listed in the `Before launch` section at the top of the run configuration. You can now 
click the `Run` button to add the run configuration and run it!

![Final run configuration](../../assets/images/level_two/module_one/final_run_config.png)

You will now see a `mypy` tab open. This tab shows output from `mypy`. It will take a bit of time for mypy to run on 
the first run of a project, so it will take a bit of time before another tab opens for the output of your code. If 
`mypy` doesn't find any type errors, your Python code will run automatically, and the output in the `mypy` tab will 
tell you there were no type errors. If `mypy` detects any type errors, it will output them and end the run which 
will prevent your Python code from running. This means you now can't run your code without making sure you don't 
have any type errors!

You will need to install `mypy` and add a run configuration for each project, but the `mypy` configuration you just 
did will save, so you won't have to enter any of the information for `mypy` in future projects. You can simply 
select it from the external-tools list and add it!
