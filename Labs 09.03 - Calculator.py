"""Labs 09.03 - Calculator"""
def main(num, result=0):
    """main"""
    for i in range(len(num)):
        result += (2+i)*min(int(num)-int("0"+"9"*i), int("9"+"0"*i))
    print(result)
main(input())
