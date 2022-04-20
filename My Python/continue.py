sum=0
for i in range(1, 11, 1):
    if i <= 3 :
        continue
    print("%d 번째 반복" %i)
    sum += i
print(sum)