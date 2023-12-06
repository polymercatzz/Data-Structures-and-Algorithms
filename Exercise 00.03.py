"""Exercise 00.03"""
def main(people):
    """Exercise 00.03"""
    for point in range(len(people)):
        noi = point
        for i in range(point+1, len(people)):
            if people[i] < people[noi]:
                noi = i
        people[point], people[noi] = people[noi], people[point]
    print(*people, sep="\n")
main([input() for i in range(int(input()))])
