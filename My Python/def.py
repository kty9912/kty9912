def func_1(a,b):
    c = a + b
    return c

d = func_1(3,6)
print(d)



def func_2(s_num, l_num, a_num):
    sum=0
    for i in range(s_num, l_num, a_num):
        sum += i
    return sum

_sum = func_2(1, 11, 1)
print(_sum)



def func_4(*args) :
    result = 0
    for i in args :
        result += i
    return result

a= func_4(1,2,3,4,5)
print(a)
