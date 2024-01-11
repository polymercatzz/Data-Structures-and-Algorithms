"""Lab 02.04"""
class ArrayStack:
    """ArrayStack"""
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            return self.data.pop()
    def is_empty(self):
        """is_empty"""
        if not self.data:
            return True
        else:
            return False
    def get_stack_top(self):
        """get_stack_top"""
        if self.size != 0:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        """get_size"""
        return self.size
    def print_stack(self):
        """print_stack"""
        return print(self.data)
def main(word):
    """Infix to Postfix"""
    result = ""
    keep = ArrayStack()
    for i in word:
        if i in "+-*/":
            while not keep.is_empty():
                if keep.get_stack_top() in "*/" or (i in "+-" and keep.get_stack_top() in "+-"):
                    result += keep.pop()
                else:
                    break
            keep.push(i)
        elif i.isalpha():
            result += i
    while not keep.is_empty():
        result += keep.pop()
    print(result)
main(input())
