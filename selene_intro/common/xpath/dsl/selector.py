from selene_intro.common.xpath.dsl.predicate import not_


def all():
    return Builder('//*')


class Builder:
    def __init__(self, selector):
        self.selector = selector

    def by(self, predicate):
        self.selector = self.selector + f'[{predicate}]'
        return self

    def by_not(self, predicate):
        self.selector = self.selector + f'[{not_(predicate)}]'
        return self

    def child(self, element='*'):
        self.selector = self.selector + f'/{element}'
        return self

    def descendant(self, element='*'):
        self.selector = self.selector + f'//{element}'
        return self

    @property
    def x(self):
        return self.selector
