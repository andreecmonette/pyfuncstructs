class Node:
    def __init__(self, data, depth):
        self._data = data
        self._depth = depth

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return str(self)

    def push(self, elem):
        if self.full():
            new = Node(data=(self, Node.new(elem, self._depth)),
                       depth=self._depth + 1)
            return new

        if self._data[-1].full():
            new = Node(data=self._data + (Node.new(elem, self._depth-1),),
                       depth=self._depth)
            return new

        new_child = self._data[-1].push(elem)
        new = self._data[:-1] + (new_child,)

        # old child nodes + new child node with push
        return Node(new, self._depth)

    def full(self):
        return len(self._data) == Vector.node_len and \
               self._data[-1].full()

    def get(self, index):
        local_i = Vector._getindex(self._depth, index)
        return self._data[local_i].get(index)

    def assoc(self, index, value):
        local_i = Vector._getindex(self._depth, index)
        new = (self._data[local_i].assoc(index, value),)
        return Node(self._data[:local_i] + new + self._data[local_i+1:],
                    self._depth)

    @classmethod
    def new(cls, elem, depth):
        node = Leaf((elem,))
        for d in range(1, depth+1):
            node = Node((node,), d)

        return node


class Leaf(Node):
    def __init__(self, data):
        assert type(data) == tuple
        return super().__init__(data, 0)

    def get(self, index):
        local_i = Vector._getindex(self._depth, index)
        return self._data[local_i]

    def full(self):
        return len(self._data) == Vector.node_len

    def push(self, elem):
        if self.full():
            new = Node(data=(self, Leaf((elem,))),
                       depth=1)
            return new

        new = self._data + (elem,)
        return Leaf(new)

    def assoc(self, index, value):
        local_i = Vector._getindex(self._depth, index)
        return Leaf(self._data[:local_i] + (value,) + self._data[local_i+1:])

class Vector:
    node_len = 2

    def __init__(self, root=None, length=0):
        if root is None:
            root = Leaf(())

        self._root = root
        self.length = length
        self.bitmask = Vector.node_len - 1

    def __str__(self):
        return str(self._root)

    def __repr__(self):
        return str(self)

    def push(self, elem):
        return Vector(self._root.push(elem),
                      length=self.length+1)

    @staticmethod
    def _getindex(depth, index):
        index >>= depth
        index &= Vector.node_len - 1
        return index

    def __getitem__(self, index):
        return self._root.get(index)

    def assoc(self, index, value):
        return self._root.assoc(index, value)

def test_create():
    v = Vector()
    return v

def test_push():
    v = Vector()
    for i in range(10):
        v = v.push(i)

    return v

def test_push2():
    v = Vector()
    for i in range(90):
        v = v.push(i)

    return v
