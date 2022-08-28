class Adverb:

    def __init__(self, f, *args, **kwargs):
        self.f = Adverb.enlist(f, *args, **kwargs) if callable(f) else f

    def __rshift__(self, other):
        return Adverb(other.f(self.f)) if other != Adverb else self.f

    def __str__(self):
        return str(self.f)

    @staticmethod
    def enlist(f, *args, **kwargs):
        return lambda x: f(*(tuple([x if i == Adverb else i for i in args]) if (Adverb in args) else (x,) + args))
