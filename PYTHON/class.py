x=input("Enter the name of the file: ")
try:
 y=open(x)
except:
    print("File cannot be opened:", x)
    quit()

e=0
for z in y:
    if z.startswith("Subject"):
        e=e+1
print(e, x)