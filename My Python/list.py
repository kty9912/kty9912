a = [[1,2],[3,4],[5,6]]
b=[]
for i in range(0, len(a), 1):
    b.insert(i,a[i][0])

print(b)