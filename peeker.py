class Element(object):
    def __init__(self, value, index, previous, future):
        self._value = value
        self._index = index
        self._previous = previous
        self._future = future
        self._first = not any(previous)
        self._last = not any(future)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self)

    def __getattr__(self, item):
        if str(self).__getattribute__(item):
            return str(self).__getattribute__(item)

    def __int__(self):
        return int(self._index)

    @property
    def value(self):
        return self._value

    @property
    def chunk(self):
        return list(reversed(self.previous)) + [self.value] + self.future

    @property
    def index(self):
        return int(self)

    @property
    def previous(self):
        return list(self._previous)

    @property
    def future(self):
        return list(self._future)

    @property
    def is_first(self):
        return self._first

    @property
    def is_last(self):
        return self._last


class Peeker(object):
    SENTINEL = object()

    def __init__(self, iterable, size):
        self._size = size
        self._sequence = enumerate(iterable, (self._size * -1) + 1)
        self._previous = [None for _ in range(size)]
        self._next = [None for _ in range(size)]
        self._index = 0
        self._current = None

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self._next) == 0:
            raise StopIteration()

        self._previous.pop()
        self._previous.insert(0, self._current)
        self._current = self._next.pop(0) if len(self._next) > 0 else None
        self._index, _value = next(self._sequence, (self._index + 1, Peeker.SENTINEL))

        if _value is not Peeker.SENTINEL:
            self._next.append(_value)

        if self._index > 0:
            _next = [x for x, _ in map(None, self._next, range(self._size))]
            return self.element(self._current, self._index, self._previous, _next)
        else:
            return self.next()

    @staticmethod
    def element(value, index, previous, future):
        return Element(value, index, previous, future)
