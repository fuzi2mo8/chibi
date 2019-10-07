import math

class Q(object):
    def __init__(self,a,b=1):
        gcd = math.gcd(a,b)
        self.a = a/gcd
        self.b = b/gcd
        self.a = int(self.a)
        self.b = int(self.b)
    
    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        return str(self.a) + '/' + str(self.b)

    def __add__(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c,b*d)

    def __sub__(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c,b*d)

    def __mul__(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*c,b*d)

    def __truediv__(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d,b*c)
        

q = Q(2,4)
print(q)
