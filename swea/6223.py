class Circle:
    def __init__(self,r):
        self.__r = r
    
    @property
    def r(self):
        return self.__r
    def a(self):
        return 3.14*(self.r)**2

cir =Circle(2)
print("원의 면적: {}".format(cir.a()))