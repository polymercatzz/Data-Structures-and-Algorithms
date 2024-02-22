"""Labs 11.02 - selectionSort()"""
import json
def main(lst, index_, times=0):
    """Labs 11.02 - selectionSort()"""
    current = 0
    for _ in range(index_):
        smalldata = current
        walker = current+1
        while walker <= index_:
            times += 1
            if lst[walker] < lst[smalldata]:
                smalldata = walker
            walker += 1
        lst[current], lst[smalldata] = lst[smalldata], lst[current]
        current += 1
        print(lst)
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
