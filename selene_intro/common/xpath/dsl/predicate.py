class Predicate:
    def __init__(self, condition=None, inverted=False):
        self._condition = condition
        self._inverted = inverted

    def __str__(self):
        return f'not({self._condition})' if self._inverted else self._condition

    def id(self, value):
        return Predicate(f'@id="{value}"', self._inverted)

    def descendant_with_text(self, value):
        return Predicate(f'.//text()="{value}"', self._inverted)

    def css_class(self, value):
        return Predicate(
            f'contains(concat(" ", normalize-space(@class), " "), " {value} ")',
            self._inverted
        )

    def and_(self, other):
        if self._condition is None:
            raise Exception('cannot be called without providing condition')
        return Predicate(f'{self._condition} and {other}')

    def or_(self, other):
        if self._condition is None:
            raise Exception('cannot be called without providing condition')
        return Predicate(f'{self._condition} or {other}')

    @property
    def not_(self):
        return Predicate(inverted=not self._inverted)
