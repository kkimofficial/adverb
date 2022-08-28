class Magrittp:

    def __init__(self, f, *args, **kwargs):
        self.f = Magrittp.f(f, *args, **kwargs) if callable(f) else f

    def __rshift__(self, other):
        return Magrittp(other.f(self.f)) if other != Magrittp else self.f

    def __str__(self):
        return str(self.f)

    @staticmethod
    def f(*args):
        return lambda x: args[0](*(tuple([x if i == Magrittp else i for i in args[1:]]) if (Magrittp in args) else (x,) + args[1:]))
