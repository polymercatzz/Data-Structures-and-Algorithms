"""Labs 10.01 - Student Class"""
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

def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())
