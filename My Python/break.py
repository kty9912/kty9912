sum=0
i=0

for i in range(1, 100, 1):
    sum += i
    if sum>=500:
        break
print("합계가 500 이상이 되는 범위의 숫자는 : %d" %i)
