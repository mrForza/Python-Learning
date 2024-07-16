class Foo:
    def __init__(self, a: int, b: int, c: str):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f'a: {self.a}'


if __name__ == '__main__':
    d = {
        'a': 1,
        'b': 2
    }
    print(Foo(**d, c='Lorem'))