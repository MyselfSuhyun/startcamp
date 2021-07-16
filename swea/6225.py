class Square:
    def __init__(self,r,t):
        self.__r = r
        self.__t = t
    
    @property
    def r(self):
        return self.__r

    @property
    def t(self):
        return self.__t
        
    def a(self):
        return self.r*self.t

Squ =Square(5,4)
print("사각형의 면적: {}".format(Squ.a()))