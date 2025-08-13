class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size + "/" + str(self._capacity)

    def deposit(self, n):
        if
        self._size += n

    def withdraw(self, n):
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
print(jar)
jar.deposit(25)
print(jar)
jar.withdraw(5)
print(jar)
#jar._capacity = 500
#print(jar)
print(jar.size)
print(jar._size)
