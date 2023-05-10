
print("Lets See Explicit Conversion")
a=str(input("Enter Number 1 -"))#this is strin right now
b=str(input("Enter Number 2 -"))#this is string right now
#print(a+b) [will give error]
print(int(a) + int(b))
 #The Change of data type done by programmer itself is known as Explicit Conversion


print("Lets See Implicit conversion Now,")

a=int(input("Enter Any Number 1 As Integer"))
b=float(input("Enter Any Number 2 As Float [To Understand Implicit conversion]"))
print(a+b)
print("Tha Data Change of Number 1 to float from int is done by python itself to prevent data loss")
