def blueberries(pints):

    lots = 0

    for i in range(pints):
        print(range(pints))
        lots += 50

    return lots


def raspberries(bushes):

    stuck = 0

    many = 0

    for i in range(bushes):

        many += 10

        if i % 4 == 0:

            stuck += 1

    return (stuck, many)


def picking(what, hungry):

    if what == "raspberries":

        pricked, count = raspberries(hungry)

    elif what == "blueberries":

        pricked = 0

        count = blueberries(hungry)

    return [pricked, count]


def main():

    day1 = picking('blueberries', 5)

    day2 = picking('raspberries', 12)

    print("Picked", day1[1], "blueberries")

    print("Picked", day2[1], "raspberries and got pricked", day2[0], "times")


main()
print(lots)
