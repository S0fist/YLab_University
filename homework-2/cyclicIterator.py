from itertools import cycle


class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.iterable:
            return i


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
