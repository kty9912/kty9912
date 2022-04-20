from re import A


a = (1,"Hello")
b = (3, 3.14)
c = a+b
d = a*3
e = a[1]
print(e)
print(a[0])

a=(10, 20, 30, 40)
print(a[1:3])
print(a[1:])
print(a[:3])

a= [20, 10, 40, 30]
b= [12, 99, 24, 55]
a.sort()
b.reverse()
print(a)
print(b)
del a[0]
b.append(22)
print(a)
print(b)
print(len(b))