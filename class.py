class Square:
    def __init__ (self,side):
        self.side = side
    def areas(self):
        return self.side**2
    def perimeter(self):
        return self.side*4
Square1 = Square(4)
print(f"Area of square:,{Square1.perimeter()}")