# Reserved words .

You cannot use reserved words as variable name / identifiers
- False: Represents the boollean false value.
- None: Represents the absence of a value or a null value.
- True: Represents the boolean true value.
- and: A logical operator that returns True if both statements are true.
- as: Used to create an alias when importing a module or in a with statement.
- assert: Used for debugging; tests if a condition is true and triggers an error if it is not
- async: Used to declare an asynchronous function or method.
- await: Pauses the execution of an asynchronous function until an awaited task completes.
- break: Immediately exits the current loop (for or while).
- class: Used to define a new user defined class (a blueprint for creating objects).
- continue: Skips the rest of the current loop iteration and moves directly to the next one.
- def: Used to define a new function.
- del: Deletes a reference to an object, such as a variable, list item, or dictionary key.
- elif: Short for "else if"; used in conditional statements to check multipel conditions sequentially.
- else: Defines a block of code to run if the if (or elif) condition is false, or if a loop completes without hitting a break.
- except: Catches and handles exceptions (errors) that occur within a try block.
- finally: Defines a block of code that will execute no matter what, even if an exception is raised in a try block.
- for: Used to create a loop that iterates over a sequence (like a list, tuple, or string).

- from: Used alongside import to import specific attributes or functions from a module.

- global: Declares that a variable inside a function refers to a variable defined at the top level of the script, rather than a local variable.

- if: Starts a conditional statement to execute code only if a specific condition evaluates to true.

- import: Used to bring an entire external module or library into your current script.

- in: Checks if a specific value is present within a sequence (like a list or string); also used in for loops.

- is: Tests for object identity, checking if two variables refer to the exact same object in memory.

- lambda: Used to create a small, anonymous (unnamed) function on a single line.

- nonlocal: Declares that a variable in a nested function refers to a variable in the nearest enclosing scope (excluding the global scope).

- not: A logical operator that reverses the boolean value of a statement.

- or: A logical operator that returns True if at least one of the statements is true.

- pass: A null statement that does nothing; used as a placeholder when syntax requires a statement but you have no code to execute yet.

- raise: Manually triggers an exception or error.

- return: Exits a function and optionally passes a value back to the caller.

- try: Starts a block of code to be tested for potential errors during execution.

- while: Creates a loop that continues executing its block of code as long as a specified condition remains true.

- with: Simplifies exception handling and resource management, commonly used for automatically closing files after opening them.

- yield: Pauses a function and returns a value like return, but saves the state to allow the function to be resumed later (creating a generator).  
 
 ## Condititonal steps
 ```python
 x = 5 
 if x < 10:
    print("smaller")
if x > 20:
    print("bigger")

print("Finis")
```
## Repeated Steps
- loops (repeated steps) have iteration variable that change each time through a loop.
```python
n = 5
while n>0:
    print(n)

print("blastoff!")
```
## Variables
- A variables is a named place in the memory where a programmer can store data and later retrive the data using the variable "name"
- Programmers get to choose the names of the variables
- You can change the contents of a variable in a later statement
```python
x=5
y=6
print(x+y)
```
## Numerical Expressions
```mermaid
flowchart TD
    MyTable["<table border='1'>
        <tr>
            <th><b>Operator</b></th>
            <th><b>Operation</b></th>
        </tr>
        <tr><td>+</td><td>Addition</td></tr>
        <tr><td>-</td><td>Subtraction</td></tr>
        <tr><td>*</td><td>Multiplication</td></tr>
        <tr><td>/</td><td>Division</td></tr>
        <tr><td>**</td><td>Power</td></tr>
        <tr><td>//</td><td>Floor Division</td></tr>
        <tr><td>%</td><td>Remainder</td></tr>
    </table>"]
```
### Operator Precedence Rules
Highest precedence rule to lowest precedence rule:
- Parentheses are always respected
- Exponentiation (raise to a power)
- Multiplication, Division, Floor Division, and Remainder
- Addition and Subtraction
- Left to right

## type function 
- In python variables, literals, and constants have a "type"
- python knows the difference between an integer number and a string 
- python knows what "type" everything is 
- some operations are prohibited 
- you cannot "add 1 " to a string 
- we can ask python what type something is by using the type() function
```python
type(eee)
>>> <class'str'>

type(1)
>>> <class'int'>
```
## several types of Numbers
- Numbers have two main types
- integers are whole numbers:
  -14, -2 ,0 ,1,100, 401233
- Floating point Numbers have decimla parts: -2.5, 0.0, 98.6, 14.0
- There are other number types -they are variations on float and integer
## Type conversions
- when you put an integer and floating point in an expression, the integer is implicitly converted to a float
- You can contol this with the build-iin function int() and float()
## Division
- Dividing integers and floating point numbers using the / operator always produces a floating point result.
```python
print(10/2)
>>> 5.0
print(99.0./100.0)
>>> 0.99

```
## Floor Division
- Division using // operator always produces a result that is the floor of the division-meaninig the result is rounded down to the nearest integer value.
```python
print(10//2)
>>> 5.0
print(9//2)
>>> 4
```
## string Conversions
- you can also use int() and float() ato convert between strings and integers
- you will get an error if the string does not contain numeric characters
 
 ## User Input
- we can instruct python to pause and read data from the user using the input() function 
- The input() fuction returns a string
``` python
name=input("who are you?")
print("welcome", name)
```
## Comments in Python
- Anything after a # is ignored by python 
- why comment?
 - - Describe what is going to happen in a sequence of code
 - - Document who wrote the code or other ancilary information
 - - Turn off a line of code - perhaps temporarily
 
 ```python
 # Get the name of the file and open it
 name= input("Enter file:")
 handle = open(name, "r")

 # Count word Frequency
 counts=dict()
 for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount in none or count > bigcount:
        bigword = word
        bigcount = count


# All done
print(bigword, bigcount)
```
# Conditional Execution
- Boolean expressions ask a qusetion and produce a YES or NO result which we use to control program flow
- Boolean expressions using comparison operators evaluate to TRUE / FALSE or YES/NO
- Comparison operators look at variables but do not change the variables
```mermaid
block-beta
    columns 2
    
    %% Header (Row 1 - Colored)
    b1["PYTHON"] b2["MEANING"]
    
    %% Row 1
    b3["<"] b4["less than"]
    
    %% Row 2
    b5["<="] b6["less than or equal to "]
    
    %% Row 3
    b7["=="] b8["equal to "]
    
    %% Row 4
    b9[">="] b10["greater than or equal to"]
    
    %% Row 5
    b11[">"] b12["greater than"]
    
    %% Row 6
    b13["!="] b14["Not equal"]

    %% Styles for Row 1 Header
    style b1 fill:#4f46e5,color:#ffffff,stroke:#312e81
    style b2 fill:#4f46e5,color:#ffffff,stroke:#312e81
```
## Indentation 
Visualizing the Block (Indentation)
In Python, you do not "close" an if statement with an endif or a closing bracket . The block is visually and logically defined entirely by whitespace (typically 4 spaces).

- Code aligned at the same indentation level belongs to the same block.

- Moving back to the left (dedenting) signals the end of that specific decision block.

To see exactly how a multi-way and nested block evaluates path-by-path, you can step through this interactive visualization:

## One-Way Decisions
- An if statement with no alternative. If the condition is True, the indented block executes. If False, the program skips it entirely.
```python
x = 10
if x > 5:
    print("x is greater than 5") 
# Execution continues here regardless

```
## Two-Way Decisions (with else)
- An if-else statement provides two strict paths. If the condition is True, the first block executes. If False, the else block executes. One of the two paths is guaranteed to run.
``` python
age = 16
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```
## Multi-Way Decisions (elif)
- Used when you have more than two mutually exclusive conditions. Python checks each condition from top to bottom. As soon as one evaluates to True, its block executes, and the rest of the chain is skipped.
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:     # Checks this only if the first 'if' is False
    print("Grade: B")
elif score >= 70:     # Checks this only if the 'elif' above is False
    print("Grade: C")
else:                 # Catch-all if everything above is False
    print("Grade: F")

```

## Nested Decisions
- Placing an if statement inside another if statement. This is used when a secondary condition should only be checked if the primary condition is already met.
```python
user_logged_in = True
is_admin = False

if user_logged_in:               # Primary decision
    print("Welcome back!")
    
    if is_admin:                 # Nested decision (indented further)
        print("Admin Dashboard Accessed")
    else:
        print("Standard User Dashboard")
```
## Python Functions
- There are two kinds of functions in python.
- Built-in functions that are provided as part of python - print(),input(),type(),float(),int()...
- functions that we define ourselves and then use
- we treeat function names as "new" reserved words (i.e., we avoid them as variable names )
## Function Definiiton
- In python a function is some reusable code that takes arguments(s) as input. does some computation, and then returns a result or results
- we define a function using the def reserved word
- we call/invoke the function by using the function name, parenteses, and arguments in an expenssion
 
 ## max function
 - A function is some stored code that we use. A function takes some input and produces an output.

 ```python
 big=max("Hello world")
 print(big)
 >>>W


 tiny = min("Hello world")
 print(tiny)
>>>' '
```
## Type conversions
- when you put an integer and floating point in an expession, the integer is implicitly converted to  a float
- you can control this with the build-in functions int() and float()

## string conversions
- you can also use int() and and float() to convert between strings and integers
- you will get an error if the string does not contain numeric characters

## Building our Own Function 
- we create a new function using the def keyword followed by optional parameters in parentheses
- we indent the body of the function
- This defines the function but does not execute the body of the function 

## Building our own Functions
- we create a new function using the def keyword followed by optional parameters in parentheses
- we indent the body of the function
- This defines the function but does not execute the body of the function


### Definitons and Uses
- once we have defined a function, we can call (or invoke) it as many times as we like
- This is the store and reuse pattern

## Arguments
- An argument is a value we pass into the function as its input when we call the function
- we use arguments so we can direct the function to do different kinds of work when we call it at different times
- we put the arguments in parentheses after the name of the function

## Parameters
A parameter is a variable which we use in the funciton definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

## Return Values
often a function will take it arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.

- A "fruitful" function is one that produces a result (or return value)
- The return statement ends the function execution and "sends back" the result of the function

### Multiple Parameters/ Arguments
- we can define more then one parameter in the function definition
- we simply add more arguments when we call the funciton
- we match the number and order of arguments and parameters

```python
def addtwo(a,b):
    added = a+b
    return added

x = addtwo(3, 5)
print(x)

>>> 8
```
## void (non-fruitfull) Functions
- when a function does not return a value, we call it a "void" function
- Functions that return values are "fruitfull" functions
- Void functions are "not frutiful"

### To funcition or not to function...
 - organize your code into "paragraphs" - capture a complete thought and name "name it"
- Don't repeat yourself - make it work once and then reuse it 
- If something gets to long or complex, break it up into logical chunks and put those chunks in functions
- make a library of common stuff that you do over and over - perhaps share this with your friends...

# Loops and Iteration
## Repeated Steps
Loops have iteration variables that change each time through a loop. often these iteration variables go through a sequence of numbers.
```python
n = 5
while n > 0 :
    print(n)
    n = n - 1
    print("Blastoff!")
    print(n)

```
## An Infinite loop
 ```python
 n=0
 while n>0:
    print("lather")
    print("rinse")
print("Dry off!")
```
## Breaking out of loop
- The break statement ends the current looop and jumps to the statement immediately following the loop
- It is like a loop test that can happen anywhere in the body of the loop
```python
while True:
    line = input(">")
    if line == "done":
        break
    print(line)
print("Done!")

```
## Finishing an Iteration with continue
  
- The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
```python
while True:
    line = input(">")
    if line[0] == "#" :
        continue
    if line == "done":
        break
    print(line)
 print("Done!")
 ```

 ## Indefinite loop 
 - while loops are called "indefinite loops" because they keep going until a logical condition becomes False
 - The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops"
 - Sometimes it is a little harder to be sure if a loop will terminate

 ## Definite Loops
 - Quite often we have a list of items of the lines in a file effectively a finite set of things
 - we can write a loop to  run that loop once for each of the items in a set using the python for construct
 - These loops are called :definite loops" because they execute an exact number of times 
 - we say that "definite loops iterate through the members of a set"
 ```python 
 # A simple Definite loops
 for i in [5,4,3,2,1]:
    print(i)
  print("Blastoff!")



  # A Definite Loop with strings
  friends = ["Joseph","Glenn","Sally"]
  for friend in friends :
    print("happy new year:", friend)
  print("Done!")
 
 ```
## A Simple Definite loop 
Definite loops(for loops) having explicit iteration variables that change each time through a loop. These iteration variable move through the sequence or set 

## Looking at in...
- The iteration variable "iterates" through the sequence (ordered set)
- The block(body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in the sequence
- The iteration variable "Iterates" through the sequence (ordered set)
- The block (body) of code is executed once for each values in the sequence
- The iteration variable moves through all of the values in the sequence 
```python
for i in [5,4,3,2,1]:
    print(i)
```
## Loop Idioms: What we do in loops
Note: Even though these examples are simples, the patterns apply to all kinds of loops

## Making "smart" loops
- The trick is "Knowing" something about the whole loop when you are stuck writting code that only sees one entry at a time 
- - -
- Set some variables to initial vlaues 
for thing in data;
- look for something or do something to each entry separately, updating a variable
- Look at the variables
## Finding the largest value
- We make a variable that contains the largest value we have seen so far. If the current number we are looking at is larger, it is the new largest value we have seen so far.
```python
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
        print(largest_so_far, the_num)

print("After", largest_so_far)
```
# More Loop Patterns...
## Counting in a loop
- To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop.
```python
zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork,thing)
print("After", zork)

```
## Summing in a loop 
- To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the vlaue to the sum each time through the loop.
```python 
zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)
```
## Finding the Average in a loop 
- An average just combines the counting and sum patterns and divides when the loop is done.
``` python
count = 0
sum = 0
print("Before", count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count,sum,value)
  print("After", count, sum, sum / count)
```
## Filtering in a loop
- We use an if statement in the loop to catch / filter the values we are looking for.
```python
print("Before")
for value in [9,41,12,3,74,15]:
    if value > 20:
        print("Large number", value)
print("After")
```
## Search using a Boolean Variable
- If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.
```python
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3 :
        found = True
        print(found, value)
    print("After", found)

```
## Finding the smallest value 
- we still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest.(the none is a void value)