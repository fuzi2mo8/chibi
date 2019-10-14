class Val(object):
    __slots__ = ['value']
    def __init__(self, v=0):
        self.value = v
    def __repr__(self):
        returen f'Val({self.value})'

e = Val(1)
e.eval()
