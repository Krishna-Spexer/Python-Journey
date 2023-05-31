list1 = [3,2,5]
print(list1)# will print whole List
print(list1[0])# will print index value of 0
print(list1[2])# will print index value of 2
print(list1[-2])#will print index value of -2 (which is 2 from the last of the list)
print(list1[len(list1)-2]) # will print value for -2 which is originally the lenght - n (n=any number)
if 7 in list1:
    print("Yes 7 is in the list")
else:
    print("No Its Not In The List")
#we can applt the same for the strings

marks=[4,5,2,"krishna",True,24,5,2,51]
print(marks)# Whole List Is Printed
print(marks[:])# Whole List is Printed
print(marks[0:]) # index 0 to last endex n is printed
print(marks[1:4])# from index 1 to index 4 is printed
print(marks[0:8:2]) # This Is Jump Index
# This Prints From Index 0 to Index 8 with a Gap Of The Jump-index Which Is 2 Here

print("Now Lets See The List Comprehension")

numbers=[1,2,3,4,5,6,7,8,9,10]
squ_numbers = [x**2 for x in numbers if x%2==0]
print(squ_numbers)
