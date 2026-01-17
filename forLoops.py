fruits=["Apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits =["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)    


fruits=["apple","banana","mango"]
for x in fruits:
    if x=="mango":
        break
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,6,2):
    print(x)

for x in range(2,10,3):
    if x== 5:
        continue
    print(x)
else:
    print("finsihed")

adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        if y == "banana":
            continue
        if y=="cherry":
            continue
        print(x,y)

for x in fruits:
    pass