class Xpath:
    def __init__(self):
        self.parts = ''

    def add(self, part):
        self.parts = self.parts + part


class XpathBuilder:
    def __init__(self):
        self._xpath = Xpath()

    def all(self):
        self._xpath.add('//')
        return self

    def by(self, predicate):
        self._xpath.add(f'{predicate}')
        return self

    def child(self, element):
        self._xpath.add(f'//{element}')
        return self

    def descendant(self):
        self._xpath.add('//*')
        return self

    @property
    def x(self):
        xpath = self._xpath
        self._xpath = Xpath()
        return xpath.parts
