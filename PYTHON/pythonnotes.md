## file handle as a sequene
- A file handles open for read can be tracked as a sequence of string where each line in the file is a string in the sequence
- we can use the following statement to iterate through a sequence 
- remember a sequence is a orderdordered set

```python
xfile=open("mbox.txt")
for cheese in xfile:
print (cheese)
```
## Counting lines in a file
- open a file read only 
- use a for loop to read each line 
- count the lines and print out the number of line

```python
fhand =open("mbox.txt")
count = 0 
for line in fhand"
    count = count + 1
print ("line count:" , count)
```
## Reading the *whole* file
- we can read the whole file ( newlines and all ) into a single 
```python
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))

print(inp[:20])
```
## Searching Through a file
- we can put an if statement in our for loop to only print lines that meet some criteria

```python
fhand=open("mbox-short.txt")
for line in fhand:
     if line.startswith("from:"):
        print(line)
```
- but the result of above code forms the new line (/n) due to print statement
- we can strip the whiltspace form the right hand side of the string used rstrip() form the string library
- The newline is considered "white space" and is stripped 
```python
fhand=open("mbox-short.txt")
for line in fhand:
    line=line.rstrip()
     if line.startswith("from:"):
        print(line)
```

## Skipping with continue
``` python 
fhand=open("mbox-short.txt")
for line in fhand:
    line=line.rstrip()
     if not line.startswith("from:"):
        continue
        print(line)
```
- we can conveniently skip a line by using the continue statement

## Using in to select lines
- we can look for a string anywhere in a line as our selection criteria
```python
fhand = open("mbox-short,txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line :
        continue 
        print(line)
```
## prompt for file name
```python
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("subject:") :
        count=count+1
print("There were", count, "subject line in ", fname)

```
### Bad File Name

```python
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("file cannot be opened:.x"):
    quit()

count = 0
for line in fhand:
    if line.startswith("subject:") :
        count=count+1
print("There were", count, "subject line in ", fname)
```





# Python lists
## programming
* Algorithms: A set of rules or steps used to solve a problem
- Data Structures: A particlar way to orginizing data in a computer

## what is not a "collection" 
Most of our variavles have one value in them - when we put a new value in the variable, the old value is overwritten

```python
x=2
x=4
print(x)
```
## A list is a Kind of collection
- A collection allows us to put many values in a single "variable"
- A collection is a nice because we can carry all many values around in one convenient package
 ``` python
 friends= ["Joseph", "Glenn", "sally"]
 carryon= ["socks", "shirt", "perfume"]
 ```
 ### List constants
 - List constants are surrounded by square brackets and the elements in the list are separated by cammas
 - A list element can be any python object-even another list
 - A list cam be empty
 ## looking inside list
 just like strinds , we can get at any single element in a list using an index specified in square brackets

```mermaid
graph TD
    X[Joseph] ~~~ n1(0)
    Y[Glenn] ~~~ n2(1)
    Z[Sally] ~~~ n3(2)

 ```
 ``` python
 friends = ["Joseph", "Glenn","Sally"]
 print(friends[1])

>>>>>Glenn
```
## Lists are Mutable
- Strings are "immutable" - we cannot change the contents of a string , we must make a new string to make any changes
- Lists are "mutable" , we can change an element of a list using the index operator
```python
fruit = "Banana"
fruit[0]="b"
>>> traceback
x=fruit.lower()
print(x)
>>> banana
lotto = [2,14,26,41,63]
print (lotto)
>>>[2,14,26,41,63]
lotto[2]=28
print(lotto)
>>>[2,14,28,41,63]
```   

  ## How Long is a list?
  - The len() function takes a list as a parameter and returns the number of elements in the list
  - Actually len() tells us the number of elements of any set or sequence (such as a strint...)
 
  ```python
  greet="hello Bob"
  print(len(greet))
  >>>9 
  x = [1,2, "joe", 99]
  print(len(x))
  >>>4
  ```
 ## Using the range function
 - The range function returns a list of numbers that range from zero to one less than the parameter
 - we can construct an index loop using for and an integer iterator
 ```python
 print(range(4))
 >>>[0,1,2,3]
 
 friends=["Joseph", "Glenn", "Sally"]
 print(len(friends))
 >>>3
 
 print(range(len(firends)))
 >>>[0,1,2,]
 ```
 ## Concatenating lists using '+'
 - We can create a new list by adding two existing lists together
```python
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
>>> [1,2,3,4,5,6]
```

## Lists can be sliced Using ':'
- Remember ':' just like in strings, the second number is "up to but not including"
```python
t = [9,41,12,3,74,15]
t[1:3]
>>> [41,12]

t[:4]
>>>[9,41,12,3]

t[3:]
>>>[3,74,15]

t[:]
>>>[9,41,12,3,74,15]
```
# List methods
 - There are several documentation in the list eg.[ 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] , to know more link is <http://docs.python.org/tutorial/datastructures.html>
 
 ## Building a list form scratch
 - we can create an empty list and then add elements using the append method
 - The list stays in order and new elements are added at the end of the list 
 ```python
 stuff = list()
 stuff.append("book")
 stuff.append(99)
 stuff.append("cookie")
 print(stuff)
 >>> ["book",99,"cookie"]
```




