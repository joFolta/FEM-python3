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

### F Strings (format strings)
- name = "Johann"
- f"Hi, my name is {name}."
=> "Hi, my name is Johann."
- string.replace("this", "that")
- **However, strings are immutable.** 
- Thus, to save the change you must save the result to a new variable. 

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
- order stays the same
- can't change the items
- defined with ( )
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
- name, age, subject, _ = student
  - _ to indicate missing item

### Sets
- **Sets store immutable types in an unsorted way** 
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

### Dictionaries
- stores key: value pairs
- keys are immutable; they are hashable
  - lists can't be keys
  - tuples can be keys
- fast item lookup by key
- dictionaries like sets have { }, but also have : (between key : value)
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

### Functions
- def this_is_a_function(params): 
  - code block here
- required arguments vs default arguments
  - function add_numbers(x, y=10):
  - x is required, but y is optional b/c it has default
- you can also specify which argument you are inputing when calling a function
  - 
- **don't use mutable types as default arguments**
  - def do_stuff(my_list=[]):
      - my_list.append("stuff")
      - return my_list
  - call function: do_stuff() => ["stuff"]
  - call function: do_stuff() => ["stuff", "stuff",]
  - call function: do_stuff() => ["stuff", "stuff", "stuff",]
  - call function: do_stuff() => ["stuff", "stuff",, "stuff", "stuff",]
  - *this is not what we intended*

  ### Booleans
  - 0 is False
  - all other numbers including -negative numbers are True
  - empty containers are False (eg. [])
    - filled containers are True (eg. [1])
  - None is False
  - bool() - checks for truthiness
    - bool(None) => Falses
    - bool(123) => True
- == is equality (checking for values, not identity)
  - (similar to === in JS), **"is"** checks for identity (do they point to the same place in memory?)
- != not equals

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