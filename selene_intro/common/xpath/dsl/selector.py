def all():
    return Builder('//*')


class Builder:
    def __init__(self, selector):
        self.selector = selector

    def by(self, predicate):
        return Builder(self.selector + f'[{predicate}]')

    def child(self, element='*'):
        return Builder(self.selector + f'/{element}')

    def descendant(self, element='*'):
        return Builder(self.selector + f'//{element}')

    @property
    def x(self):
        return self.selector
