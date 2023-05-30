a = int(input("Enter Any Number - "))
b = int(input("Enter Any Number - "))

def isgreater(a,b):
    if a>b:
        print("Number",a,"Is Greater")
    elif a==b:
        print("Number Are Equal")
    else:
        print(b,"Is Greater")


def islower(a,b):
    if a>b:
        print(b,"Is Smaller")
    elif a==b:
        print("Numbers Are Equal")
    else:
        print(a,"Is Greater Or Equal")

def iseven():
    pass

def calculatemean(a,b):
    gmean = (a*b)/(a+b)
    print(gmean)

#We Have Defined The Functions And We Can Use Them Without Typin Codes Again And Again

isgreater(a,b)
islower(a,b)
calculatemean(a,b)


d = int(input("Enter Any Number - "))
c = int(input("Enter Any Number - "))

print("Now Lets Calcute For The Latest Numbers")

isgreater(c,d)
islower(c,d)
calculatemean(c,d)
