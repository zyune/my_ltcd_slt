def fruit(berries):

    pears = 0.0
    # print("berry is ", berries)

    # for rasp in range(len(berries)):
    #     pears += berries[rasp]
    for rasp in berries:  # mark 1
        #     print("rasp is ",rasp)
        pears += rasp

    return pears/len(berries)


def landscape(bushes):

    truck = []

    for sprout in range(bushes):

        truck.append(5.0 + sprout)

    return truck


def highway(cars):

    pollution = []

    for passenger in range(cars):

        pollution.append(5)

    return pollution


def enhance(what):

    for whoknows in range(len(what)):

        what[whoknows] += 3


def main():

    blue = landscape(3)  # mark 2

    green = landscape(5)

    red = blue

    # mark 3

    yellow = highway(5)

    magenta = highway(3)

    cyan = magenta

    enhance(magenta)

    enhance(green)

    print(fruit(blue))

    print(fruit(green))

    print(fruit(red))

    print(fruit(yellow))

    print(fruit(magenta))

    print(fruit(cyan))


main()
