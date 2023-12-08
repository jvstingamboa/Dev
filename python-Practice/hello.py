print("Hello world!")

number = 333

print(number)

if number < 5:
    print("number is less than 5")
else:
    print("number is greater than 5" )

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old.")

Person.say_hello(Person("John", 36))


def addOnetoNumber(num):
    return print(num+1)

addOnetoNumber(999)

list = [1, 3,4,5,513,4,5,64,5,4,5,34,1325,24,624,423,5234,123,234,]

sortedList = sorted(list, reverse=True)

print(sortedList)