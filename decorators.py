'''def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())



def lowercase(func):
    def inner():
        return func().lower()
    return inner()

@lowercase
def name():
    return "Hello World"
    
print(name())

def changecase(func):
    def uppercase():
        return func().upper()
    return uppercase


@changecase
def myfunc():
    return "My name"

@changecase
def myfunc2():
    return "My school"

print(myfunc())
print(myfunc2())



def changecase(myfunc):
    def uppercase():
        return myfunc().upper()
    return uppercase



@changecase
def myfunc2(name):
    return "his name is" + name

print(myfunc2("Hari"))



#decorators with args and kwargs
def mychangecase(func):
    def myinner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return myinner

@mychangecase
def func(name):
    return "My name is " + name

print(func("Pranish"))




def changecase(myfunc):
    def innerfunc(*args,**kwargs):
        return myfunc(*args,**kwargs).upper()
    return innerfunc

@changecase
def func1(name):
    return "My name is " + name

print(func1("Hari"))


def changecase(n):
    def changecase(func):
        def case():
            if n==0:
                a= func().lower()
            else:
                a= func().upper()
            return a
        return case
    return changecase

@changecase(0)
def funny():
    return "haRI"
print(funny())
            '''
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

