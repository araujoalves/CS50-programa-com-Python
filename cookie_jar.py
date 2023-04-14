class Jar:
    def __init__(self, capacity=12):  
        self.capacity = capacity  
        self.size = 0  

    def __str__(self):  
        
        if self.size <= self.capacity:
            return '🍪' * self.size
        else:
            raise ValueError('Jar is full')

    def deposit(self, n):  
        if self.size > self.capacity: 
            raise ValueError("Jar is full")
        self.size += n

    def withdraw(self, n):  
        self.size -= n
        if self.size < 0:
            raise ValueError("Jar is emply")

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        if capacity < 0:  
            raise ValueError('The jar is too small')
        self.capacity = capacity

    def get_size(self):
        return self.size

    def set_size(self, n):
        self.size = n


jar = Jar()
jar.deposit(3)
jar.withdraw(1)
jar.deposit(6)
print(jar)
