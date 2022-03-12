class Fruit():

    def __init__(self, name, size, tartness):

        self.name = name

        self.size = size

        self.tartness = tartness

    def getName(self):

        return self.name

    def getSize(self):

        return self.size

    def howTart(self):

        if self.tartness > 5:

            return 'tart'

        return 'sweet'

    def howBig(self):

        if self.size > 5:

            return 'large'

        return 'small'


class Strawberry(Fruit):

    def __init__(self):

        Fruit.__init__(self, 'strawberry', 3, 4)


class Lemon(Fruit):

    def __init__(self):

        Fruit.__init__(self, 'lemon', 5, 9)


def howBig(self):

    return 'medium'


class Watermelon(Fruit):

    def __init__(self):

        Fruit.__init__(self, 'watermelon', 9, 3)


class Cherry(Fruit):

    def __init__(self):

        Fruit.__init__(self, 'cherry', 2, 6)


def main():

    fruits = [Lemon(), Strawberry(), Cherry(), Watermelon()]  # mark 1

    for f in fruits:

        print("A "+f.getName()+" is a "+f.howBig() +
              ", "+f.howTart()+"fruit")  # \mark 2


main()
