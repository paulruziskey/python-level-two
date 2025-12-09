# Strings

## String Literals

### Basic String Literals

Enclosing text inside either single quotes or double quotes creates a *string literal*. String literals can then be 
assigned to variables to create `str` objects. The following code demonstrates creating a string from a string literal.

```python
sentence = 'Hello, world!'
```

It's not important whether you choose to use single quotes or double quotes for your string literals. What's 
important is *being consistent*. This means picking a style and sticking with it. One common style is to pick one 
type of quote and stick with it for every string literal. Another style is to use double-quoted string literals for 
strings that will be displayed to a user and to use single-quoted string literals for all other strings.

#### Escape Sequences

We can also include *escape characters* in string literals. Escape characters are characters formed by escaping 
another character with the *escape character* (`\`). We can use these escape characters to include newlines and tabs 
in strings, among other things. The following code demonstrates using escape characters for newline (`\n`) and tab 
(`\t`).

```python
print("\tEach\nword\nwill\nbe\non\nits\nown\nline")
```

The above code outputs the following to the console.

```
    Each
word
will
be
on
its
own
line
```

We can also use the escape character to help us output characters we would otherwise have trouble with. For example, 
in single-quoted strings, we can't write single quotes because Python would see it as the end of the string literal 
instead of a quote. The same applies to double quotes in double-quoted strings. A similar problem exists when trying 
to write a backslash character in a string literal since backslash is the escape character. The following code 
demonstrates how we can output double quotes and backslashes using escape characters.

```python
print("Here is a \"backslash\": \\")
```

The above code outputs the following to the console.

```
Here is a "backslash": \
```

### Multiline String Literals

Sometimes we want to write strings which would end up spanning multiple lines in the console. This means we would 
need to include a lot of newline characters, which would make it a bit hard to read the string. This is where 
*multiline string literals* come in! Multiline string literals let us create strings that span multiple lines in our 
code, and any formatting in multiline string literals becomes part of the final string! This means if we indent 
within a multiline string literal, the indentation will be in the actual string! The following code demonstrates 
creating a string from a multiline string literal.

```python
dialog = '''It was time to write some code.
    "Hello, world!" said the code.
    "Goodbye, code!" said the programmer, fearing his creation had
become sentient.'''
print(dialog)
```

The above code outputs the following to the console.

```
It was time to write some code.
    "Hello, world!" said the code.
    "Goodbye, code!" said the programmer, fearing his creation had
become sentient.
```

Notice how the indentations and the newlines are part of the string? This means we can write strings spanning 
multiple lines without having to use escape sequences! Quotes also don't need to be escaped since multiline string 
literals are created by using either triple single quotes or triple double quotes, meaning they won't interfere. 
Definitely make use of multiline string literals when you need a string that spans multiple lines.

#### Delimiter Convention

While you can use both triple single quotes and triple double quotes to create multiline string literals, you should 
prefer triple single quotes. This is because triple-double-quoted multiline string literals are used to create 
something called a *docstring* which we learn about in Python Level Three. This convention helps differentiate them 
from each other.

#### Formatting Details

Multiline string literals are formatted relative to the left margin of our code. The first line is formatted 
relative to the opening delimiter (i.e., `'''` or `"""`). This is the case regardless of the relative indentation 
level of the code around a multiline string literal. This can make multiline string literals a bit confusing to 
program with. The following code demonstrates the details of multiline-string-literal formatting.

```python
choice = input("Would you like some text? ")
if choice == "yes":
    text = '''Here is
    some text'''
else:
    text = "No text for you"
print(text)
```

The above code outputs the following to the console.

```
Would you like some text? yes
Here is
    some text
```

Notice how "some text" is indented even though it doesn't look like it in the code? The following code demonstrates 
how to properly write the multiline string literal to avoid this indentation.

```python
choice = input("Would you like some text? ")
if choice == "yes":
    text = '''Here is
some text'''
else:
    text = "No text for you"
print(text)
```

The above code outputs the following to the console.

```
Would you like some text? yes
Here is
some text
```

This is certainly annoying since we have to go against the relative indentation of the code in the if-statement to 
get the formatting we want. While multiline string literals can be helpful in some situations, it may be preferable 
to avoid them to write cleaner code.

Additionally, the formatting around the delimiters matters. The following code demonstrates some interesting 
formatting due to seemingly innocuous formatting around the multiline-string-literal delimiters.

```python
choice = input("Would you like some text? ")
if choice == "yes":
    text = '''
    Here is
    some text
    '''
else:
    text = "No text for you"
print(text)
print("Follow-up text")
```

The above code outputs the following to the console.

```
Would you like some text? yes

    Here is
    some text
   
Follow-up text
```

The multiline string literal kept the newline after the opening delimiter and the newline before the closing 
delimiter. This had the added effect of indenting the first line of text since its formatting is no longer dependent 
on the opening delimiter. Keep these formatting rules in mind when working with multiline string literals.

Additionally, multiline string literals can be turned into other kinds of literals like f-string literals in the 
same way regular string literals can.

### String Literals and Concatenation

Python automatically concatenates adjacent string literals without the need for the addition operator (`+`). This is
because Python will turn the adjacent string literals into one big string literal during compilation. The addition
operator is only needed when combining strings at runtime. The following code demonstrates concatenation of string
literals.

```python
combined_literal = "hello" "world"
print(combined_literal)
```

The above code outputs the following to the console.

```
helloworld
```

This can be done across multiple lines by surrounding the string literals in parentheses. This is similar to using a
multiline string literal, but without any formatting.

```python
paragraph = (
    "This is the start of my paragraph."
    "Here is the second line of my paragraph. It's not a very interesting line."
    "Maybe this third line will help."
)
print(paragraph)
```

The above code outputs the following to the console.

```
This is the start of my paragraph.Here is the second line of my paragraph. It's not a very interesting line.Maybe this third line will help.
```

This paragraph doesn't look much like a paragraph. Since multiline string literals are the only kind of literal which
remembers formatting, we need to use escape characters if we want that with concatenated string literals.

```python
paragraph = (
    "This is the start of my paragraph.\n"
    "Here is the second line of my paragraph. It's not a very interesting line.\n"
    "Maybe this third line will help."
)
print(paragraph)
```

The above code outputs the following to the console.

```
This is the start of my paragraph.
Here is the second line of my paragraph. It's not a very interesting line.
Maybe this third line will help.
```

Whether you make use of concatenated string literals or multiline string literals is up to you! It's also worth mentioning
that it doesn't matter what kind of string literal is used. All string literals can be concatenated with all other string
literals. The following code demonstrates concatenating a multiline string literal with an f-string literal.

```python
fav_num = 7
paragraph = (
    """Here is my cool paragraph.
It works properly because it uses a multiline string literal."""
    f"\nI know you didn't ask, but my favorite number is {fav_num}."
)
print(paragraph)
```

The above code outputs the following to the console.

```
Here is my cool paragraph.
It works properly because it uses a multiline string literal.
I know you didn't ask, but my favorite number is 7.
```

## String Methods

### `len` Method and Indexing

If we want to get the length of a string (i.e., the number of Unicode characters), we can use the `len` function.

If we want to get a character at a particular index value, we can use the *subscript operator* (`[]`) to do so.

The following code demonstrates the `len` function and the subscript operator.

```python
word = "hello"
print(f"{word} has {len(word)} character(s) in it!")
print(f"{word} starts with the letter {word[0]}")
```

It's common to check if strings are empty, and we can do this with the `len` function by checking if the length of a 
string is equal to zero, but the more Pythonic way is to treat the string like a boolean. All Python objects that 
support the `len` function have this ability. The following code shows how we can treat a string like a boolean to 
ask if it's empty.

```python
user_input = input("Enter something: ")
if not user_input:  # same as len(user_input) == 0
    print("I asked nicely...")
else:
    print("Thank you!")
```

What if we wanted to get the last letter in word? We would need to use the `len` function to get the last index 
value. This is demonstrated in the following code.

```python
print(f"{word} ends with the letter {word[len(word) - 1]}")
```

This is a little annoying since it makes everything longer. Luckily for us, Python supports *negative indexing* 
which lets us index from the end of the string instead of the beginning! The following code does the same thing as 
the above code.

```python
print(f"{word} ends with the letter {word[-1]}")
```

`-1` is essentially syntactic sugar for `len(word) - 1`. You can think of it like we have omitted the `len(word)` 
part and kept the `- 1`. This means that `-n` means `len(word) - n`. This definitely makes the code nicer to read 
and write. However, it's possible to get bugs in Python that would actually be errors in other languages due to 
Python allowing negative index values, so that should be kept in mind.

### Substrings Using Slices

We can also get a substring by using a `slice` object. Slices are created using colons within the subscript operator.
Slices can be created outside the subscript operator, but we'll cover that later. Slices can be a little difficult 
to wrap your head around at first, but once you play with them a bit, you'll see they're very simple!

Creating a slice allows us to define a particular range of a sequence that you want. Slices have the following syntax.

```
start:stop:step
```

These are actually the same three values we can pass to the `range` function! This means creating a slice is similar 
to creating a range. The slice `3:7:1` creates a slice starting from index-value 3, ending at index-value 6, and 
incrementing by 1. Just like ranges, the ending value is *exclusive*. The following code demonstrates this slice in 
action.

```python
word = "perseverance"
print(word[3:7:1])
```

The above code outputs the following to the console.

```
seve
```

It's very common to want slices where the increment is 1. Just like with ranges, we can define slices without 
specifying the increment, and Python will assume 1. The above code could be written as follows.

```python
word = "perseverance"
print(word[3:7])
```

It's also common to want slices starting from the beginning of a string and slices going to the end of a string. 
Python will also assume 0 for the starting index value if unspecified, and `len(string)` for the ending index value 
if unspecified. The following code demonstrates this.

```python
word = "hello"
print(word[:3])  # same as 0:3
print(word[2:])  # same as 2:len(word)
```

The above code outputs the following to the console.

```
hel
llo
```

This means it's super easy to get every other letter or every third letter in a string using a slice! The following 
code demonstrates this.

```python
word = "perseverance"
print(word[::2])
```

The above code outputs the following to the console.

```
preeac
```

It's necessary to write two colons because Python would take the 2 as being the ending index value if there were 
only one colon.

Slices also work with negative index values and negative increments!

```python
word = "hello"
print(word[::-1])  # prints the string backwards
print(word[:-1])  # prints all but the last character
```

The above code outputs the following to the console.

```
olleh
hell
```

What, then, is the simplest slice we can make? That would be `:`! The following code demonstrates making a copy of a 
string using a slice.

```python
word = "hello"
word_copy = word[:]
print(word_copy)
```

#### Slices and Performance

Slices always create copies in Python. While this might not seem like a bad thing, it means Python has to do the 
work of creating a new string every time we use a slice. As you start to work with slices, think about whether 
copying is okay and whether you might actually want a different solution to avoid the performance cost.

### Inclusion

If we want to check if a string contains a particular character or substring, we can use the `in` operator. We can 
use the operator alone to check for a particular character or substring as written, or we can use the `casefold` 
method to specify that the check should be done *case-insensitively*. This means that we could ask if a string 
contains the letter a by only checking 'a' case-insensitively. The following code demonstrates both uses of the 
Contains method.

```python
word = 'Apple'
print('a' in word)  # case-sensitive
print('a' in word.casefold())  # case-insensitive
```

The above code outputs the following to the console.

```
False
True
```

The `casefold` method returns a copy of the original string with as many characters as possible converted to their 
lowercase variants. This does incur a bit of a performance penalty, so it's wise to call `casefold` once and store 
the result, then use that result as many times as necessary to avoid making more than one copy of the original string.

If we want to get the index value of the first occurrence of a particular substring, we can use the `find` method. 
The following code demonstrates this.

```python
word = 'apple'
print(f"Index of 'p': {word.find('p')}")
```

The above code outputs the following to the console.

```
Index of 'p': 1
```

If the `find` method can't find any occurrences of the substring, it returns -1. The following code demonstrates 
this. While also showing off using the `casefold` method to do a case-insensitive search.

```python
word = 'apple'
print(f"Index of 'z': {word.casefold().find('z')}")
```

The above code outputs the following to the console.

```
Index of 'z': -1
```

Since the `casefold` method converts characters to lowercase, it's important to make sure other string literals are 
using only lowercase letters.

### Equality

If we want to check if two strings are equal, we use the *equals operator* (`==`). Additionally, we can use the 
`casefold` method to perform the check case-insensitively.

```python
word_1 = 'apple'
word_2 = 'APPLE'
print(word_1 == word_2)  # case-sensitive
print(word_1.casefold() == word_2.casefold())  # case-insensitive
```

The above code outputs the following to the console.

```
False
True
```

### Ordering

We can check the ordering of strings in Python as well. Python strings are ordered *lexicographically* which simply 
means they're ordered alphabetically. Since this is Python, the most obvious way to do this is the right way to do 
it. We simply use the relational operators (`<`, `<=`, `>`, `>=`) to compare strings alphabetically. Once again, the 
`casefold` method can be used to make the comparison case-insensitive.

```python
word_1 = 'apple'
word_2 = 'banana'
word_3 = 'APPLE'
print(word_1 <= word_2)  # case-sensitive
print(word_1 <= word_3)
print(word_1.casefold() <= word_2.casefold())  # case-insensitive
print(word_1.casefold() <= word_3.casefold())
```

The above code outputs the following to the console.

```
True
False
True
True
```

The first true makes sense since "apple" comes before "banana" in the alphabet. The reason for the false is because 
'A' actually comes before 'a' in Unicode, and the comparison was case-sensitive. The second true is because "apple" 
still comes before "banana"; case doesn't affect this answer. We then get true for the last answer since "apple" and 
"APPLE" are the same word when compared case-insensitively.

### Parsing Helpers

It's often desirable to get rid of stray whitespace around a string when we need to parse it. Python strings have a 
`strip` method which strips leading and trailing whitespace characters. You can also use this method to strip other 
things besides whitespace characters, but you'll mostly use it to strip whitespace characters.

```python
stripped_input = input("Enter something: ").strip()
print(f"You entered: \"{stripped_input}\"")
```

The above code outputs the following to the console.

```
Enter something:          okay       
You entered: "okay"
```

## String Immutability

Strings in Python are *immutable*. This means they can't be changed once created. Even though a lot of string 
methods in Python seem like they modify a string, they're actually creating a copy with the modified property and 
returning that. This is important to know because it can affect the performance of your code. We'll learn 
a big consequence of this in a later module.
