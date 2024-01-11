"""Lab 05.05"""
class DataNode:
    """DataNode"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        """getdata"""
        return self.data

    def set_data(self, data):
        """setdata"""
        self.data = data

    def get_next(self):
        """getnext"""
        return self.next

    def set_next(self, ndata):
        """setnext"""
        self.next = ndata
class SinglyLinkedList():
    """SinglyLinkedList"""
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        """"print"""
        start = self.head
        if start:
            while start.get_next():
                print(start.get_data(), "->", end=" ")
                start = start.get_next()
            print(start.get_data(), end="")
        else:
            print("This is an empty list.")
    def insert_last(self, lastdata):
        """last"""
        pnew = DataNode(lastdata)
        if not self.head:
            self.head = pnew
        else:
            start = self.head
            while start.get_next():
                start = start.get_next()
            start.set_next(pnew)
        self.count += 1
    def insert_front(self, fontdata):
        """front"""
        pnew = DataNode(fontdata)
        if not self.head:
            self.head = pnew
        else:
            front = self.head
            self.head = pnew
            self.head.set_next(front)
        self.count += 1
    def insert_before(self, node, bedata):
        """before"""
        pnew = DataNode(bedata)
        try:
            start = self.head
            before = self.head.get_next()
            if start.get_data() == node:
                pnew.set_next(start)
                self.head = pnew
            else:
                while True:
                    if before.get_data() == node:
                        pnew.set_next(before)
                        start.set_next(pnew)
                        break
                    start = start.get_next()
                    before = before.get_next()
            self.count += 1
        except(TypeError, ValueError, ArithmeticError, AttributeError):
            print("Cannot insert, %s does not exist."%node)
    def delete(self, data):
        """del"""
        try:
            start = self.head
            before = self.head.get_next()
            if start.get_data() == data:
                self.head = before
                del start
            else:
                while True:
                    if before.get_data() == data:
                        start.set_next(before.get_next())
                        del before
                        break
                    start = start.get_next()
                    before = before.get_next()
            self.count -= 1
        except(TypeError, ValueError, ArithmeticError, AttributeError):
            print("Cannot delete, %s does not exist."%data)

def main():
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
