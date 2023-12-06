"""Exercise 00.05"""
class Person:
    """hello"""
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
class Project:
    """project"""
    def __init__(self, name, member):
        """name"""
        self.name = name
        self.member = member
    def showprojectname(self):
        """p nameproject"""
        print("Hello There! This is %s"%self.name)
    def showmembers(self):
        """p member"""
        print("This project has %s members"%(len(self.member)))
        for i in self.member:
            person = Person(i[0], i[1])
            person.say_hello()
def main():
    """main"""
    name = input()
    member = sorted([(input(), input()) for i in range(int(input()))])
    data = Project(name, member)
    data.showprojectname()
    data.showmembers()
main()
