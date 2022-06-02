import self as self


class SparseArray:
    def __init__(self, A):
        self.orig = A
        self.storage = {}
        for idx, elem in enumerate(A):
            if elem != None:
                self.storage[idx] = elem

    def __len__(self):
        return len(self.storage)

    def __getitem__(j, self):
        return self.storage[j]

    def __setitem__(j, e, self=None):
        self._storage[j] = e

sparse = [None]*1000 + [1] + [None]*1000 + [2]

new_sparse = SparseArray(sparse)

print(len(new_sparse))