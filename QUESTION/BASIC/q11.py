class Calci:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    def sqroot(self):
        print(self.n**1/2)
a = Calci(4)
a.square()
a.cube()
a.sqroot()