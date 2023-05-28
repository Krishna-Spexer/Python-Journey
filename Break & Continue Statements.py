#Break Statement
for i in range(10):
    if i==5:
        print(i)
        break


#continue statements
for i in range(12):
    if (i==10):
        print("skipped iteration")
        continue
    print("5 x ",i,"=",5*i)


#Do - While Loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
