x = 4 # x is a variable here to match
match x: #Match Statement Starts From Here
    #if X is 0
    case 0:
        print("X is 0")
    #if X is 4
    case 4:
        print("X is 4")
        
    case _:  #This Is The Default Case (Works Like Else Function)
        print(x)
