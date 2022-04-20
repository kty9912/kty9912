import pandas as pd

pd_list = pd.Series([5000, 6000, 6500, 6500],   index=["아메리카노", "카페라떼", "키페모카", "카푸치노"])

print(pd_list)
print("스리즈의 값 : ",pd_list.values)
print("스리즈의 인덱스 값 : ",pd_list.index)

