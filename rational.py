class Q(object):
    def __init__(self,a,b=1):
        self.a = a
        self.b = b
    
    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        return str(self.a) + '/' + str(self.b)

    def add(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c,b*d)

    def sub(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c,b*d)

    def mul(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*c,b*d)

    def truediv(self,q):
        a = self.a 
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d,b*c)
        

q1 = Q(1,2)
q2 = Q(1,3)
print(q1.add(q2))
print(q1.sub(q2))
print(q1.mul(q2))
print(q1.truediv(q2))