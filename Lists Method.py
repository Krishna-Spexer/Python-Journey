l=[1,56,27,315,1,27,88,531,67]
l.append(0)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print("This Method Provides The Index Of Any Element Which Is Already Present In The List, Which Is",l.index(56),"For The Value of 315")
print('This Shows The Occurance Of Any Value In The List',l.count(1))
m = l.copy()
print(l)
print(m)
c = [13,'hy',891,10,1,6001]
m.extend(c)
print(m)
print(l.count(315))
m.insert(1,0)
print(m)
a=[1,2]
b=[3,4]
ac = a + b
print(ac)
