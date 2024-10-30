class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"My name is {self.name}.I am {self.age} years old and a {self.gender} . ")
myobject=Person("Glory",23,"female")
myobject.display()