'''
def myfunc():
    x=300
    print(x)
    def innerfunc():
        print(x)
    innerfunc()


x=300
def myfunc():
    x=200
    print(x)

myfunc()
print(x)


x=300
def myfunc():
    global x
    x=300
    print(x)
myfunc()
print(x)


#non local keyword
def myfunc():
    x="Jane"
    def myfinc2():
        nonlocal x
        x="Hopper"
    myfinc2()
    return x
print(myfunc())


#nonlocal
def myfunc():
    x="Jane"
    def myfunc2():
        nonlocal x
        x ="hello"
    myfunc2()
    return x

print(myfunc())

'''
x="Global"
def outer():
    x="enclosing"
    def inner():
        x="local"
        print("Inner:",x)
    inner()
    print("Outer:",x)

outer()