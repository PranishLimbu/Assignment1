def my_functions():
        print("Hello this is my favourite function")

my_functions()
my_functions()
my_functions()
my_functions()

def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit-32)*5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(67))

def whats_your_name(name):
        return ("My name is",name)

print(whats_your_name("Ram"))
print(whats_your_name("Hari"))
print(whats_your_name("Shyam"))


def get_greeting():
        return "Hello from a function"
message=get_greeting()
print(message)

def my_functions(fnames):
        print(fnames+"Refsnes")

my_functions("mail")
my_functions("Tobias")
my_functions("Linus")


def sec_functions(*kids):
        print("The youngest child is"+kids[2])
sec_functions("Email","Tobias","Linus")


def thir_functions(*kids):
        print("The youngest child is"+kids[1])


thir_functions("Email","Jonas","kids")

def four_function(*args):
        print("Type:",type(args))
        print("Type:",type(args[1]))
four_function("string",1)


def five(*args):
        print(args)

five("Pranish",1,1.2)

def six(greetings,*args):
        for name in args:
                print(greetings,args)
six("Pranish","Philip")

def my_functions(greeting,*names):
        for name in names:
                print(greeting,name)
my_functions("Hello","Email","Tobias","Linus")


def your(greetings,*role):
        for roles in role:
                print(greetings,roles)

your("Hello","QA","BA")

def natural(good,*life):
        for lifes in life:
                print(good,lifes)
natural("Good","water","food","shelter")

def greeting(greetings,*name):
        for names in name:
                print(greetings,names)
greeting("Hello:","Pranish","Kumar","Samsohang","Limbu")


def total(*numbers):
        total=0
        for num in numbers:
                total +=num
        return total

print(total(1,2,3,4,5))

def my(*numbers):
 if len(numbers)==0:
         return None
 max_num =numbers[0]
 for num in numbers:
        if num>max_num:
                max_num=num
        return max_num
 

print(my(1,2,3,4,5,6,7,8,9))


def my_key(**kid):
        print("His last name is"+kid["lname"])
my_key(fname="Tobias",lname="refnses")


def my_func(**name):
        print("Type:",type[name])
        print("Name:",name["fname"])
        print("Age:",name["age"])
        print("Data",name)
        print("City",name["city"])

my_func(fname="Pranish",age=20,city="KTM")









def data(**datas):
        print("NAME:",datas["name"])
        print("AGE:",datas["age"])
        print("Gender:",datas["gender"])


data(name="Pranish",age=20,gender="MALE")


def mydata(email,**details):
        print(email)
        print("additional details")
        for key,values in details.items():
                print(key + ":" , values)
mydata("pranish@gmail",age=20,address="Kathmandu")



def argg(email,*args,**kwargs):
        print("email:",email)
        print("positional",args)
        print("dict",kwargs)
argg("email@123","Person","Game",age=20,name="Pranish")



def sum(a,b,c):
        return a+b+c
numbers=[1,2,3]
print(sum(*numbers))

def listt(name,age,city):
        print("name:",name)
        print("age:",age)
        print("city:",city)
data={"name":"Pranish","age":20,"city":"Kathmandu"}
print(listt(**data))


def kwargss(fname,lname):
        print("Hello",fname,lname)
person={"fname":"Pranish","lname":"limbu"}
kwargss(**person)