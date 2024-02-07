"""Labs 09.02 - isIntersect(A, B, C)"""
import json
def main(lis1, lis2, lis3):
    """list"""
    for i in lis1:
        if i in lis2 and i in lis3:
            return print(True)
    return print(False)
main(json.loads(input()), json.loads(input()), json.loads(input()))
