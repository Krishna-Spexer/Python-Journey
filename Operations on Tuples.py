print("There is no direct method to manuplate a tuple, for manuplating a tuple you have to 1st convert it into a list.")
tup1 = (1,241,53,5,3,"3","hy")
temp = list(tup1)
temp.append("Krishna")
temp.pop(1) # removes the index
temp[0]= "Zero"
tup1= tuple(temp)
print(tup1)
print(len(tup1))
print(type(tup1[0]))
print(tup1[:])
print(tup1[2:])
print(tup1[:4])
print(tup1[:-4])
a = input("Select Any Number From The Brackets (53,241,20,13,\"yo\") - ")
if a and int(a) in tup1 :
    print ("Yes",a,"is present in the tuple")
else:
    print("Better Luck Next Time")
