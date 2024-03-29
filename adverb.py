class Adverb:

    def __init__(self, f, *args, **kwargs):
        self.f = Adverb.enlist(f, *args, **kwargs) if callable(f) else f
        self.unwrap = False

    def __rshift__(self, other):
        if other == Adverb:
            return self.f
        elif other.unwrap:
            return other.f(self.f)
        else:
            return Adverb(other.f(self.f))

    def __add__(self, other):
        if other == Adverb:
            result = Adverb(self.f)
            result.unwrap = True
            return result
        return Adverb(lambda x: other.f(self.f(x)))

    def __str__(self):
        return str(self.f)

    @staticmethod
    def enlist(f, *args, **kwargs):
        return lambda x: f(*(tuple([x if i == Adverb else i for i in args]) if (Adverb in args) else (x,) + args))
