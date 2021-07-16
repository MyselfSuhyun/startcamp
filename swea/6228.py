class Shape:
    def a(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.__length =length

    @property
    def length(self):
        return self.__length
    
    def a(self):
        return "정사각형의 면적: {0}".format(self.length**2)

Squ =Square(3)
print(Squ.a())