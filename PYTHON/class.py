x=input("Enter the name of the file: ")
y=open(x)
e=0
for z in y:
    if z.startswith("Subject"):
        e=e+1
print(e, x)