class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, v=0):
        self.value = v
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

#v = Val(1)
#assert v.eval() == 1

def toExpr(a):
    if not isinstance(a,Expr):
        a = Val(a)
    return a

class Binary(Expr):
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'

class Add(Binary):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = toExpr(a)
        self.right = toExpr(b)
    def eval (self):
        return self.left.eval() + self.right.eval()

class Mul(Binary):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = toExpr(a)
        self.right = toExpr(b)
    def eval (self):
        return self.left.eval() * self.right.eval()

class Sub(Binary):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = toExpr(a)
        self.right = toExpr(b)
    def eval (self):
        return self.left.eval() - self.right.eval()

class Div(Binary):
    __slot__=['left','right']
    def __init__(self,a,b):
        self.left = toExpr(a)
        self.right = toExpr(b)
    def eval (self):
        return self.left.eval() / self.right.eval()



#v = Div(Div(6,2),3)
#print(v.eval())
#assert v.eval()

#assert isinstance(Val(1),Expr)
#assert isinstance(Div(Val(7),Val(2)),Expr)
