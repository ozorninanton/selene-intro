def all():
    return Builder()


class Builder:
    def __init__(self):
        self.parts = '//'

    def by(self, predicate):
        self.parts = self.parts + predicate
        return self

    def child(self, element=None):
        self.parts = self.parts + f'//{element if element else "*"}'
        return self

    @property
    def x(self):
        return self.parts
