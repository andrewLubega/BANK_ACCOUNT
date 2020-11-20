# A Sample class with init method
class Person:

    # init method or constructor
    def init(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Shwetanshu")
p.say_hi()
