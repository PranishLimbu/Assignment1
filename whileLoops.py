i=1
while i <6:
    print(i)
    i=i+1

i=1
while i<6:
    print(i)
    if i==3:
        break
    i=i+1

i=1
while i<6:
    i=i+2
    if i==3:
        continue
    print(i)

i=4
while i<6:
    i=i+1
    if i==5:
        continue
    print(i)

i=5
while i>1:
    i=i-1
    print(i)
    if i==1:
        break

i=4
while i<7:
    i=i+1
    print("Weekday")
else:
    print("Saturday")