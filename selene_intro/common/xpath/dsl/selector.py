from selene_intro.common.xpath.dsl.predicate import not_


def all():
    return Builder('//*')


class Builder:
    def __init__(self, selector):
        self.selector = selector

    def by(self, predicate):
        return Builder(self.selector + f'[{predicate}]')

    def by_not(self, predicate):
        return Builder(self.selector + f'[{not_(predicate)}]')

    def child(self, element='*'):
        return Builder(self.selector + f'/{element}')

    def descendant(self, element='*'):
        return Builder(self.selector + f'//{element}')

    @property
    def x(self):
        return self.selector
