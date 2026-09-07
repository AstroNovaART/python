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

