"""Lab 07.01"""
class BSTNode():
    """classBST"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        """get data"""
        return self.data

    def set_data(self, data):
        """set data"""
        self.data = data

    def get_left(self):
        """get left"""
        return self.left

    def set_left(self, left):
        """set left"""
        self.left = left

    def get_right(self):
        """get right"""
        return self.right

    def set_right(self, right):
        """set right"""
        self.right = right

def main():
    """mmain"""
    p_new = BSTNode(int(input()))
    print(p_new.get_data(), p_new.get_left(), p_new.get_right(), sep="\n")
main()
