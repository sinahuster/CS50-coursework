class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size + "/" + str(self.capacity)

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        pass

    @property
    def size(self):
        pass


jar = Jar()
print(jar)
jar.deposit(25)
print(jar)
jar.withdraw(5)
print(jar)
