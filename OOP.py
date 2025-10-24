# Classes -> Objects -> Methods -> Inheritance -> Polymorphism -> Encapsulation -> Abstraction

class MyClass:
    pass

p1 = MyClass()
# print(p1.x)
p2 = MyClass()
p3 = MyClass()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printAge(self):
        print("My age is " + str(self.age))

    def myPrint(self):
        print("My name is " + self.name)
        self.printAge()
    
    def incAge(self, years):
        self.age += years
    
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __del__(self):
        pass
    
p1 = Person("John", 36)
p1.age = 40
# del p1.age
p1.city = "New York"
print(p1.name, p1.age, p1.city)
p1.myPrint()
p1.incAge(5)
p1.myPrint()



# [5] -> [4] -> [3] -> None


class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

llist = LinkedList()
llist.append(5)
llist.append(4)
llist.append(3)
llist.printList()


# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def printStudentID(self):
        print("My student ID is " + str(self.student_id))

s1 = Student("Alice", 20, "S12345")
s1.myPrint()
s1.printStudentID()
s1.printAge()

print(len('Hello'))
print(len([1, 2, 3, 4, 5,6,7,8,9]))
print(len({'a': 1, 'b': 2, 'c': 3}))

# Polymorphism
class Animal:
    def speak(self):
        pass    
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    animal.speak()
    print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
# animal_sound(dog)
# animal_sound(cat)

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance   

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
print(account.__balance)  # Accessing private attribute (not recommended)
