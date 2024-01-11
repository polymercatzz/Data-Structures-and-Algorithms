"""Lab 05.02"""
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

def main():
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()
