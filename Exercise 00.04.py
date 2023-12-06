"""Exercise 00.04"""
class Person:
    """main"""
    def __init__(self, name, age):
        """name age"""
        self.name = name
        self.age = age
    def get_details(self):
        """p name age"""
        print("%s, %s years old"%(self.name, self.age))
    def say_hello(self):
        """p name"""
        print("Hello, my name is %s!"%self.name)
def main():
    """main"""
    result = Person(input(), input())
    result.get_details()
    result.say_hello()
main()
