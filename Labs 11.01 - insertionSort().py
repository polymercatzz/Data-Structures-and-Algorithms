"""Labs 11.01 - insertionSort()"""
import json
def main(lst, index_, times=0):
    """Labs 11.01 - insertionSort()"""
    current = 1
    for _ in range(current, index_+1):
        walker = current-1
        while walker >= 0:
            times += 1
            if lst[walker+1] < lst[walker]:
                lst[walker], lst[walker+1] = lst[walker+1], lst[walker]
            else:
                break
            walker -= 1
        print(lst)
        current += 1
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
