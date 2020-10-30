# FEM-python3
🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
![Frontend Masters Logo](img/FrontendMastersLogo.png)
🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
Project created from Frontend Masters workshop: 
"A Practical Guide to Python - An immersive hands-on Python Course" 
-by *Nina Zakharenko*

Slides Website: https://practical.learnpython.dev/

### 🥚 Easter egg (Python Philosophy)
- Enter REPL (>>>) in terminal with "python"
- type "import this"

*The Zen of Python, by Tim Peters*

*Beautiful is better than ugly.*
*Explicit is better than implicit.*
*Simple is better than complex.*
*Complex is better than complicated.*
*Flat is better than nested.*
*Sparse is better than dense.*
*Readability counts.*
*Special cases aren't special enough to break the rules.*
*Although practicality beats purity.*
*Errors should never pass silently.*
*Unless explicitly silenced.*
*In the face of ambiguity, refuse the temptation to guess.*
*There should be one-- and preferably only one --obvious way to do it.*
*Although that way may not be obvious at first unless you're Dutch.*
*Now is better than never.*
*Although never is often better than *right* now.*
*If the implementation is hard to explain, it's a bad idea.*
*If the implementation is easy to explain, it may be a good idea.*
*Namespaces are one honking great idea -- let's do more of those!*

## 🐍 Style Convention: snake_case
- lower case words
- use underscore for spacing

### File Names
- filename.py
- use snake_case
- all lowercase
- short
- .pyc files
  - don't commit these to git - add to .gitignore
  - intermediary python compiled files
  - don't worry about them

*Everything is a object in Python*
*True + True => 2*
*True = 1*
*False = 0*

### Keywords:
- None 
- True
- False
- list
- str
- \backslash to ignore ("escape character")
- \n new line
- \t new tab

### Helpful REPL (>>>) methods:
- type() - checks type of a variable
- dir() - show me all the methods for this type
  - eg. dir(str)
    - ignore double underscore ones
    - lists all methods for str
- help()
  - eg. help(str.isalpha)
    - help on method (str.isalpha) / class (like str)
    - space to scroll down
    - q to exit

### Numbers/Math in Python
- integers
  - type(5) 
  - int(5.2) => 5
- floats 
  - type(5.2) 
  - float(3) => 3.0
- complex
   - type(25p)

- power
  - 2 ** 3 => 2x2x2 => 8
- min
  - min(1, 5, -3) => -3
- max
- round
  - round(3.1) => 3
  - round(3.9) => 4

+= increment
-= decrement

### Print()
- print("hi)
  - hi
- print("hi", 5)
  - hi 5
- concatenation
  - "hi" + "bye"
    - "hibye"
- **pretty print** - module (included in standard library, but must bring in)
  - from pprint import pprint
  - adds line breaks when commas are there (\n)

### Strings
- **F Strings (format strings)**
- name = "Johann"
- f"Hi, my name is {name}."
=> "Hi, my name is Johann."
- string.replace("this", "that")
- **However, strings are immutable.** 
- Thus, to save the change you must save the result to a new variable. 
- String.split(what_to_split_with)
  - my_string = "Nina,Max,Mark"
  - my_string.split(",")
  - my_string => ['Nina', 'Max', 'Mark']
- String.join()
  - can add custom strings (ie. " - ") betwen the parts being joined
- #### Slicing
  - my_string = "Hello, world!"
    - my_string[7:12] # from 7 to 12
    - 'world'
  - my_string[:12]
    - start at 0
  - my_string[7:]
    - go to the end
  - quick copy of entire string or list
    - my_string[:]
  - start from the end
    - my_string[-1]
    - my_string[-1:-6]

### Lists
- **Lists are mutable - can be changed.** 
- [ square brackets ] - declared with square brakcets
- names = ["Johann", "Sam", "Suzie",]
  - trailing commas are encourages
- methods:
  - len(list)
  - list[index]
  - sorted(list)
    - **this does NOT change original list**
    - optionally, reverse list
      - sorted(list, reverse=True)
  - list.sort()
      - **this DOES change original list**
  - list.append(12345)
    - adds to end of list
  - list.insert(position_to_insert, 55)
    - list.insert(0, 55)
    - inserts 55 at position 0 (beginning of list)
  - list[index] = "relace list item with this string at index number"
  - item **in** list
    - returns True or False
  - To find out more about list methods
    - dir(list) - finds all methods
    - help(list.count) - info about a specific method

### Tuple
- **Tuples are immutable - can NOT be changed.** 
- can’t change them once they’ve been created. Tuples are great for moving data around in a lightweight way, because you can *unpack them easily into multiple variables*.
- order stays the same
- can't change/reassign the items
  - my_tuple[0] = "new value" => ERROR
- defined with ( )
  - person = ('Jim', 29, 'Austin, TX')
    - name, age, hometown = person
    - name => 'Jim"
    - age => 29
    - hometown => 'Austin, TX'
- my_tup = ()
- type(my_tup)
  - <class 'tuple'>
- **make sure you add a trailing comma to a tuple (especially if only single item in tuple)**
  - tuu = ("ji")
  - type(tuu) => <class 'str'>
  VS
  - tuup = ("hi",)
  - type(tuup) => <class 'tuple'>
- matching left side items with right side items
- *unpacking to variables*
  - name, age, subject, _ = student
    - _ placeholder to indicate missing item
    - or else, ERROR: too many errors to unpack

### Sets
- **Sets are mutable; they store immutable types in an unsorted way** 
- Sets are a great data type for storing unique data - you can only have one of any given object in a set. Sets are **unordered** (*can't access by index*), thus you can’t access them with [] indexing syntax, but they do have some handy functions.
- A set is a mutable datatype that allows you to store immutable types in an unsorted way. Sets are mutable because you can add and remove items from them. They can contain immmutable items, like tuples and other primitive types, but not lists, sets, or dictionaries which are themselves mutable.
Unlike a list or a tuple, a set can only contain one instance of a unique item. There are no duplicates allowed.
The benefits of a set are: very fast membership testing along with being able to use powerful set operations, like union and intersection.
- While lists are generally used to store collections of similar items together, tuples, by contrast, can be used to contain a snapshot of data.
- A set is a mutable datatype that allows you to store immutable types in an unsorted way. 
- sets are fast
- fun hash function
- doesn't have to check every item to find it
- empty set
  - set()
- sets can't contain duplicate values
- {3, 3, 4} => {3, 4}
- set() removes duplicates
- shortcut to check for mutability
  - hash(5) => yes
  - hash([]) => ERROR
- order does not matter; is not guaranteed
  - can't do my_set[0]
- my_set.discard("Nina")
  - removes "Nina" from set
- my_set.update(add items from here)
- my_set.add(4)

### Dictionaries
- stores key: value pairs
- keys are immutable; they are hashable
  - lists can't be keys
  - tuples can be keys
- fast item lookup by key
- dictionaries like sets have { }, but also have : (between key : value)
- no order, can't use index
- however, the values are mutable
- my_dict[key]
  - my_dict["hair_color"]
  - NOPE X - my_dict[0]
  - searches by key
- Methods:
  - dict.get("key", "default returned if not found")
    - dict.get("hair_color")
  - dict1.update(dic2)
    - will add dic2 to dic1
  - dic.keys()
    - returns only keys
  - dic.values()
    - returns only values
  - **dic.items()**
    - key AND value pairs
  - deleting keys from dictionaries
    - del my_dict["hair_color"]
    - prefered method, is dict.pop()
      - you can also set a default return, if not found (prevents an exception)
  - "hair_color" in my_dict
    - returns True or False

### Functions
- def this_is_a_function(params): 
  - code block here
- required arguments vs default arguments
  - function add_numbers(x, y=10):
  - x is required, but y is optional b/c it has default
- you can also specify which argument you are inputing when calling a function
  - You can also use the argument's keyword. This helps with readability
  - def calculate_numbers(x, y, operation="add"):
      ...
  - calculate_numbers(2, 3) // argument with default param is optional
  - calculate_numbers(x=2, y=3, operation="subtract")
- **don't use mutable types as default arguments**
  - def do_stuff(my_list=[]):
      - my_list.append("stuff")
      - return my_list
  - call function: do_stuff() => ["stuff"]
  - call function: do_stuff() => ["stuff", "stuff",]
  - call function: do_stuff() => ["stuff", "stuff", "stuff",]
  - call function: do_stuff() => ["stuff", "stuff",, "stuff", "stuff",]
  - *this is not what we intended*

### Mutable or Immutable?
- use hash() function to check
- if immutable, hash() => no error
  - hash(21) => works, b/c immutable
  - hash(my_tuple) => works, b/c immutable
- if mutable (can change), hash() => ERROR
  - hash([1, 2, 3]) => ERROR
  - hash({3, 4}) => ERROR

### Booleans
- 0 is False
- all other numbers including -negative numbers are True
- empty containers are False (eg. [])
  - filled containers are True (eg. [1])
- None is False
- use "is" for None, False, and True
  - don't use == for these
- bool() - checks for truthiness
  - bool(None) => Falses
  - bool(123) => True
- == is equality (checking for values, not identity)
  - (similar to === in JS), **"is"** checks for identity (do they point to the same place in memory?)
- != not equals
- use 5 > 3
- don't use 5 > 3 == True

### and, or. not
- and
  - are both values True?
- or
  - is at least one True?
- not
  - the opposite
  - negates what you have

### if statements
- if 5 > 3:
    print("always print")
- **if b == True:**
  - don't do this!
  - do this instead:
    - **if b:**
- if:
  else:

### loops
- **for ... in:**
  - code bock here
- for num in **range**(3, 7):
  - print(num) 
    - 3
    - 4
    - 5
    - 6
- **enumerate**
  - 
- looping though dictionary
  - my_dict.items()

## Practical Applications
### List Comprehensions
- List comprehensions are a unique way to create lists in Python. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be any kind of Python object.

List comprehensions will commonly take the form of [<value> for <vars> in <iter>].
- square brackets b/c it's a list
- [what_i_want for item in list]
- [len(name) for name in names]
- my_new_list = [len(name) for name in names]

- (optionally) add a condition to the end
- my_new_list = [len(name) for name in names CONDITION]
- my_new_list = [len(name) for name in names if len(name) % 2 == 0 ]
  - (only add to new list if name length is even)

### Generator Comprehension
- A generator comprehension looks just like a list comprehension, except we use parentheses instead of brackets.
- Generator expressions are a more advanced concept. A generator is a type of iterable object - like a list, you can iterate through each element - however, unlike a list, generators evaluate elements on demand, instead of assembling them all at once.
- Not stored in memory; gets used up

### Working with Files
- different modes for opening files
- cheatsheet: https://practical.learnpython.dev/05_practical_applications/40_working_with_files/
- my_file = open("my_file.txt") // by default read mode
- my_file = open("my_file.txt", "w") // write mode
- my_file = open("my_file.txt", "a") // add to end if it exists
- need to call close() after finished so it closes it from memory and doesn't lock it up
  - solution: Context Managers ~ try/catch block
  - with open("my_file.text") as my_file:
    - contents = my_file.read()
  - no need to close anymore
- list of dictionaries
  - import json
  - with open("cities.json") as cities_file:
    - cities_data = json.load(cities_file)
    - print(cities_data)

    - => [{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, {'name': 'Philadelphia', 'pop': 1567442}]

    - from pprint import pprint
    - pprint(cities_data)
    - => [{'name': 'New York', 'pop': 8550405},
    -     {'name': 'Los Angeles', 'pop': 3971883},
    -     {'name': 'Chicago', 'pop': 2720546},
    -     {'name': 'Houston', 'pop': 2296224},
    -     {'name': 'Philadelphia', 'pop': 1567442}]