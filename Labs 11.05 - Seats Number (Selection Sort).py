"""Labs 11.05 - Seats Number (Selection Sort)"""
import json
def main(lst, index_, times=0):
    """Labs 11.05 - Seats Number (Selection Sort)"""
    current = 0
    for _ in range(index_):
        smalldata = current
        walker = current+1
        while walker <= index_:
            times += 1
            if lst[walker][0] < lst[smalldata][0] or \
                (lst[walker][0] == lst[smalldata][0] and \
                int(lst[walker][1:]) < int(lst[smalldata][1:])):
                smalldata = walker
            walker += 1
        lst[current], lst[smalldata] = lst[smalldata], lst[current]
        current += 1
        print(lst)
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
