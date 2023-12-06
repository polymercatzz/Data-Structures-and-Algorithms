"""Exercise 00.02"""
def main(place, time_):
    """Exercise 00.02"""
    print((place == "Outdoor" and time_ >= 240) or (place == "Indoor" and time_ >= 480))
main(input(), float(input()))
