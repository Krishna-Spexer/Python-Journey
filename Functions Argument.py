def avg(a=7,b=9):
    print("The Avg Is",(a+b)/2)
avg()

def avg3(a,b,c=2):
    print("avg is",(a+b+c)/3)
avg3(1,4)

def avg4(*numbers):
    for i in numbers:
        print(i)
avg4(1,9)

def avg5(**numberss):
    for x in numberss:
        print(x)

avg5(e='6',f='8',g='1',h='8')


#not much clear though 
