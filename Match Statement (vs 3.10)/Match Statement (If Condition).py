x =int(input("Enter The Value Of X - "))# x is a variable here to match
match x: #Match Statement Starts From Here
    #if X is 0
    case 0:
        print("X is 0")
    #if X is 4
    case 4:
        print("Case Is 4")
    case _ if x != 90:
       print("X is Not 90")
    case _ if x > 10:
       print("X is Greater Than 10")
    case _:  #This Is The Default Case (Works Like Else Function)
        print(x)
print("The Last Case Is The Default Case Which Is The Last Option And Works Similar Like Else In If-Else Function")

