name = "krishna tyagi"
for i in name:
    print(i)

print("It Was A Simple Loop Now Lets Try some more")

fruits=['Apple','Mango','Banana','Pineapple']
for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i)

print("We Tried Some New Things, Now Lets Use The Range() Function")

for x in range(5):
    print(x)
print("This range function printed value from 0 to 4 , but what if we want it 1 to 5")
for y in range(5):
    print(y+1)
print("If We Want To Start our Loop From Middle To Some Specific Number Then We Can Do range(x,y)")
for z in range(2,8):
    print(z)
for k in range(2,29,5):
    print(k)#my predicted output is 2,7,12,17,22,27

'''in for loop increment by default is 1. but if u want to overwrite that so you have to use step parameter for that.
for k in range(1,12,3)
in this example 1 is start point 12 is till u want to go and 3 is steps which is u overwrited.
output:
1
4
7
10'''
