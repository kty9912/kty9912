a ={"name" : "test", "age": 20, "phone": "01012345678"}
print(a)
print(a["name"])
a["age"] = 25
print(a)
a["area"]="Seoul"
print(a)

print(list(a.keys()))
print(a.values())
print(a.items())
del(a["phone"])
print(a)