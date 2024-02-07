"""Labs 09.01 - Summation (Type 1)"""
def main(num, result=0):
    """01"""
    for i in range(1, num+1):
        result += int(i)
    print(result)
main(int(input()))
