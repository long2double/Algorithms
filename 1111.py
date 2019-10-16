import random


def shuffle(array):
    for i in range(len(array)):
        index = random.randint(0, len(array) - 1)
        array.append(array.pop(index))
    return array


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    shuffle(a)
    print(a)