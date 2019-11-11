class A:
    def __init__(self):
        print('1111')

    def __new__(cls):
        print('2222')
        return object.__new__(cls)


if __name__ == '__main__':
    a = A()
