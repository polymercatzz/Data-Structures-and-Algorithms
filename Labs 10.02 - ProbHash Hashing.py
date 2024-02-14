"""Labs 10.02 - ProbHash Hashing"""
class Student():
    """Student Class"""
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        """id std"""
        return self.std_id

    def get_name(self):
        """name"""
        return self.name

    def get_gpa(self):
        """gpa"""
        return self.gpa

    def print_detail(self):
        """print details"""
        print("ID: %d"%self.std_id)
        print("Name: %s"%self.name)
        print("GPA: %.2f"%self.gpa)

class ProbHash():
    """ProbHash"""
    def __init__(self, size):
        self.hash_table = [" "]*size
        self.size = size

    def hash(self, key):
        """hash"""
        return key%self.size

    def rehash(self, hkey):
        """rehash"""
        rehkey = self.hash(self.hash(hkey)+1)
        while self.hash_table[rehkey] != " ":
            rehkey = self.hash(rehkey+1)
            if rehkey == self.hash(hkey):
                return None
        return rehkey

    def insert_data(self, student):
        """insert_data"""
        hkey = self.hash(student.get_std_id())
        if self.hash_table[hkey] == " ":
            self.hash_table[hkey] = student
            return print("Insert %d at index %d"%(student.get_std_id(), hkey))
        rhkey = self.rehash(hkey)
        if rhkey != None:
            self.hash_table[rhkey] = student
            print("Insert %d at index %d"%(student.get_std_id(), rhkey))
        else:
            print("The list is full. %d could not be inserted."%student.get_std_id())

    def search_data(self, std_id):
        """search_data(std_id):"""
        hkey = self.hash(std_id)
        while True:
            if self.hash_table[hkey] != " " and self.hash_table[hkey].get_std_id() == std_id:
                print("Found %d at index %d"%(std_id, hkey))
                return self.hash_table[hkey]
            hkey = self.hash(hkey+1)
            if hkey == self.hash(std_id):
                print("%d does not exist."%std_id)
                return None
def main():
    """main"""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
