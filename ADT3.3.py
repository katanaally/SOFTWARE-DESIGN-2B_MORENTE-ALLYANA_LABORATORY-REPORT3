class PositionalList:

    class Position:

        def __init__(self, element, index=0):
            self._element = element
            self._index = index
            self._size = 0

        def element(self):
            return self._element

    def __init__(self):
        self._sequence = []
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError('Must be a proper position type')

        return p._index

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._sequence[0]

    def last(self):
        return self._sequence[-1]

    def after(self, p):
        data = self._validate(p)
        return self._sequence[data + 1]

    def before(self, p):
        data = self._validate(p)
        return self._sequence[data - 1]

    def add_first(self, e):
        """Adds an element at the front of the list"""
        new = self.Position(e, 0)
        self._sequence.append(new)
        self._size += 1
        return new

    def add_last(self, e):
        new = self._make_position(e, self._size + 1)
        self._sequence.append(new)
        self._size += 1
        return new

    def add_after(self, p, e):

        if self.is_empty():
            raise ValueError('Empty')
        data = self._validate(p)
        new = self.Position(e, data + 1)  # new element is after p
        self._sequence.insert(data + 1, new)
        for j in range(new._index + 1, len(self._sequence)):
            self._sequence[j]._index += 1  # adjust indexes accordingly
        self._size += 1
        return new

    def add_before(self, p, e):

        if self.is_empty():
            raise ValueError('Empty')
        data = self._validate(p)
        new = self.Position(e, data)
        self._sequence.insert(data, new)
        for j in range(new._index + 1, len(self._sequence)):
            self._sequence[j]._index += 1
        self._size += 1
        return new

    def delete(self, p):
        data = self._validate(p)
        for j in range(len(self._sequence) - 1, data, -1):  # until p is reached
            self._sequence[j]._index -= 1  # decrement indexes
        return self._sequence.pop(p._index)

    def replace(self, p, e):
        if not isinstance(p, self.Position):
            raise ValueError('Must be a proper position type')
        old = p._element
        p._element = e
        return old

    def __repr__(self):
        return str([(x._element, x._index) for x in self._sequence])
