"""Exercise 02.03"""
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
    """main"""
    parentheses = ArrayStack()
    square = ArrayStack()
    curly = ArrayStack()
    num_paren = 0
    num_square = 0
    num_curly = 0
    for i in word:
        if i == "(":
            parentheses.push(i)
            num_paren += 1
        elif i == ")":
            parentheses.pop()
            num_paren -= 1
        elif i == "[":
            square.push(i)
            num_square += 1
        elif i == "]":
            square.pop()
            num_square -= 1
        elif i == "{":
            curly.push(i)
            num_curly += 1
        elif i == "}":
            curly.pop()
            num_curly -= 1
    return not (num_curly or num_paren or num_square)
print(main(input()))
