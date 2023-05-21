a=(int(input("Enter Any Number - ")))                 # Input Taken
if a==10:                                             # If Started From Here
    print("The Number is Equal to 10")
elif a>15:                                            # Used Elif Here
    print("The Number Is Greater Than 15")
elif a!=0:                                            # You Can Use Elif No. Of Times
    print("The Number Is Not Equal To 0")
    if a<10:                            # From Here We Have Started Nested If Else Function (Using If Else Inside Elif/If)
        print("The Number Is Smaller Than 15")
    elif a>10:                                        # Continuing Nested
        print("The Number Is Greater Than 10")
    elif a <= 20:
        print("The Number Is Equal Or Smaller Than 20")
    elif a >= 20:
        print("The Number Is Equal Or Greater Than 20")
    else:                              #Completed Nested Function Here By Ending The If/Else Loop
        print("Input The Number Once Again")
else:                                   #Ended The Main/1sr If/Else Loop Here
    print("Please Enter A Valid Input")
print("In This Code We Have Used All The Conditional Operators \n If-Else,If-Elif-Else And Nested too")
