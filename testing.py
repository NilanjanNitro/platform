class A:
    a: int

    def __init__(self, cn: int):
        self.a = 1
        self.a = self.a + cn
        print(self.a)
        # A.a = A.a + cn
        # print(A.a)


def main():
    c1 = A(1)
    c2 = A(1)
    c3 = A(1)


if __name__ == "__main__":
    main()
