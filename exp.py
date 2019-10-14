class Val(object):
    __slots__ = ['value']
    def __init__(self, v=0):
        self.value = v
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
assert v.eval() == 1

class Add(object):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = a
        self.right = b
    def eval (self):
        return self.left.eval() + self.right.eval()

class Mul(object):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = a
        self.right = b
    def eval (self):
        return self.left.eval() * self.right.eval()

class Sub(object):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = a
        self.right = b
    def eval (self):
        return self.left.eval() - self.right.eval()

class Div(object):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = a
        self.right = b
    def eval (self):
        return self.left.eval() / self.right.eval()



v = Div(Div(Val(6),Val(2)),Val(3))
print(v.eval())
assert v.eval()

