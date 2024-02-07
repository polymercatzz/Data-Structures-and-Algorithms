# """Lab 07.05"""
# class BSTNode():
#     """classBST"""
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def get_data(self):
#         """get data"""
#         return self.data

#     def set_data(self, data):
#         """set data"""
#         self.data = data

#     def get_left(self):
#         """get left"""
#         return self.left

#     def set_left(self, left):
#         """set left"""
#         self.left = left

#     def get_right(self):
#         """get right"""
#         return self.right

#     def set_right(self, right):
#         """set right"""
#         self.right = right
# class BST():
#     """BST na ja"""
#     def __init__(self):
#         self.root = None

#     def get_root(self):
#         """ give root"""
#         return self.root

#     def set_root(self, root):
#         """set root"""
#         self.root = root

#     def insert(self, data):
#         """insert_"""
#         pnew = BSTNode(data)
#         if not self.root:
#             self.root = pnew
#         else:
#             start = self.root
#             while start:
#                 if data < start.get_data() and start.get_left():
#                     start = start.get_left()
#                 elif data >= start.get_data() and start.get_right():
#                     start = start.get_right()
#                 else:
#                     break
#             if data < start.get_data():
#                 start.set_left(pnew)
#             else:
#                 start.set_right(pnew)
#     def preorder(self, root=None):
#         """preorder():"""
#         if root:
#             print("->", root.get_data(), end=" ")
#             if root.get_left():
#                 self.preorder(root.get_left())
#             if root.get_right():
#                 self.preorder(root.get_right())
#         else:
#             self.preorder(self.root)
#     def is_empty(self):
#         """emmty"""
#         return bool(not self.root)
#     def inorder(self, root=None):
#         """inorder"""
#         if root:
#             if root.get_left():
#                 self.inorder(root.get_left())
#             print("->", root.get_data(), end=" ")
#             if root.get_right():
#                 self.inorder(root.get_right())
#         else:
#             self.inorder(self.root)
#     def postorder(self, root=None):
#         """postorder"""
#         if root:
#             if root.get_left():
#                 self.postorder(root.get_left())
#             if root.get_right():
#                 self.postorder(root.get_right())
#             print("->", root.get_data(), end=" ")
#         else:
#             self.postorder(self.root)
#     def traverse(self):
#         """print"""
#         if self.is_empty():
#             return print("This is an empty binary search tree.")
#         print('Preorder: ', end='')
#         self.preorder()
#         print('\nInorder: ', end='')
#         self.inorder()
#         print('\nPostorder: ', end='')
#         self.postorder()
#     def find_min(self):
#         """min"""
#         if not self.root:
#             return None
#         else:
#             start = self.root
#             while start.get_left():
#                 start = start.get_left()
#             return start.get_data()
#     def find_max(self):
#         """max"""
#         if not self.root:
#             return None
#         else:
#             start = self.root
#             while start.get_right():
#                 start = start.get_right()
#             return start.get_data()
#     def delete(self, data):
#         """delete"""
#         try:
#             start = self.root
#             before = start
#             while True:
#                 if start.get_data() == data and start != self.root:
#                     if not start.get_left() and not start.get_right():
#                         if data < before.get_data():
#                             before.set_left(None)
#                         else:
#                             before.set_right(None)
#                     elif start.get_left() and not start.get_right():
#                         if data < before.get_data():
#                             before.set_left(start.get_left())
#                         else:
#                             before.set_right(start.get_left())
#                     elif not start.get_left() and start.get_right():
#                         if data < before.get_data():
#                             before.set_left(start.get_right())
#                         else:
#                             before.set_right(start.get_right())
#                     break
#                 elif data < start.get_data():
#                     before = start
#                     start = start.get_left()
#                 elif data >= start.get_data():
#                     before = start
#                     start = start.get_right()
#         except(TypeError, ValueError, ArithmeticError, AttributeError):
#             start = self.root
#             if start.get_data() == data:
#                 if not start.get_right() and not start.get_left():
#                     self.root = None
#                 elif not start.get_right() and start.get_left():
#                     self.root = start.get_left()
#                 elif start.get_right() and not start.get_left():
#                     self.root = start.get_right()
#             else:
#                 print("Delete Error, %s is not found in Binary Search Tree."%data)


# def main():
#     """main"""
#     my_bst = BST()
#     while 1:
#         text = input()
#         if text == "Done":
#             break
#         condition, data = text.split(": ")
#         if condition == "I":
#             my_bst.insert(int(data))
#         elif condition == "D":
#             my_bst.delete(int(data))
#         else:
#             print("Invalid Condition")
#     my_bst.traverse()

# main()
# x = input().split()
# print(x[0], x[1])
data_id = []
data_grades = []
grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
while True:
    n = input()
    if n == "q":
        break
    n = n.split()
    data_id.append(n[0])
    data_grades.append(n[1])
g = input().split()
for i in g:
    who_index = data_id.index(i)
    grades_index = grades.index(data_grades[who_index])
    if grades_index:
        data_grades[who_index] = grades[grades_index-1]
for i,j in enumerate(data_id):
    print(j, end=" ")
    print(data_grades[i])
