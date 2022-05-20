"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.num = start

    def generate(self):
        """Generate a new number by adding one"""
        self.num = self.num + 1
        print(self.num)
        return self.num
    
    def reset(self):
        """Reset the generated number back to the original number"""
        self.num = self.start
        print(self.num)
        return self.num


serial = SerialGenerator(start=100)

serial.generate()

serial.generate()

serial.generate()

serial.reset()

serial.generate()