from math import cos,acos
class AngleToBig(Exception):

    pass
class SideSum(Exception):
    pass
class Triangle():
    A,B,C = None, None, None
    AB,BC,CA = None,None, None
    def __init__(self , A=1, B=1, C=1 , AB=60, BC=60 , CA=60):
        self.A = A
        self.B=B
        self.C = C
        self.AB= AB
        self.BC = BC
        self.CA= CA
    def modify_angle(self,angle,degrees):

        var= self.__getattribute__(angle)
        self.__setattr__(angle, self.__getattribute__(angle)+degrees)
        if (degrees < 0) or  (var>180):
            raise AngleToBig
      
        self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.angle)) ** (1 / 2)
        if (self.angle + self.BC + self.CA) <= 180:
            self.BC = degrees(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
            self.CA = degrees(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))
        print("Self angle=AB= ", self.angle, "Recalculated BC angle: ", self.BC, "Recalculated CA angle: ", self.CA,
              sep='\n')
          return var
    def modify_side(self,side ,metters):
        var1= self.__getattribute__(side)
        self.__setattr__(side,self.__getattribute__(side)+metters)
        if (self.A + self.B) <= self.C or (self.B + self.C) <= self.B or (self.A + self.C) <= self.B:
            raise SideSum
        if self.side <= 0:
            raise ValueError
        self.side += self.meters
        self.B = ((self.side + 1) / self.side) * self.B
        self.C = ((self.side + 1) / self.side) * self.C
        print('Side A(self side): ', self.side, 'Side B:', self.B, 'Side C:', self.C

        return var1

t= Triangle()
t.modify_angle('AB',10)
print(t.modify_angle('AB',6))
t.modify_side('C',6)
print(t.modify_side('C',6))
