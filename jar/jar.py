class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must not be a negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must not be a negative number")
        if self._size + n > self._capacity:
            raise ValueError("Exceeds the cookie jar's capacity")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must not be a negative number")
        if self._size < n:
            raise ValueError("Not enough cookies in the cookie jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    print(jar)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()