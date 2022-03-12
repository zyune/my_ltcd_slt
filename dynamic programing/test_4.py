def share(baskets, what, left):

    if left == 0:

        return

    print("there are %d %s" % (baskets[left-1], what[left-1]))

    share(baskets, what, left-1)  # mark 1


def main():

    plots = [6, 3, 5, 4, 2]

    plants = ['strawberries', 'pears', 'peaches', 'apples', 'mangos']

    share(plots, plants, len(plots))


main()

