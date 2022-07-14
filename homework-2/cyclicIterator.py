from itertools import cycle


# Встроенный метод cycle.
class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        for r in self.iterable:
            return r


if __name__ == "__main__":
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
