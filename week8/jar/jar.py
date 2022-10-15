class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return (self.size) * "🍪"



    def deposit(self, n):
        try:
            n = int(n)
        except ValueError:
            pass
        else:
            if (self.capacity > self.size) and ((self.size + n) <= self.capacity):
                self.size = self.size + n
            else:
                raise ValueError("At capacity")


    def withdraw(self, n):
        try:
            n = int(n)
        except ValueError:
            pass
        else:
            if (self.size > 0) and (self.size - n >= 0) :
                self.size = self.size - n
            else:
                raise ValueError("At capacity")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity


    @size.setter
    def size(self, size=0):
        self._size = size



def main():
    jar = Jar(capacity=20)
    print(f"Capacity: {jar.capacity}")

    print(f"size: {jar.size}")

    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)





if __name__ == "__main__":
    main()