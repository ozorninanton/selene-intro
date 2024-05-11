class Predicate:
    def __init__(self, expression=None, not_=False):
        self.expression = expression
        self.__not = not_

    def __str__(self):
        return self.expression

    def id(self, value):
        return Predicate(self.__apply_not_(f'@id="{value}"'))

    def descendant_with_text(self, value):
        return Predicate(self.__apply_not_(f'.//text()="{value}"'))

    def css_class(self, value):
        return Predicate(
            self.__apply_not_(
                f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'
            )
        )

    def __apply_not_(self, expression):
        if self.__not:
            return f'not({expression})'
        else:
            return expression

    def and_(self, predicate):
        return Predicate(f'{self.expression} and {predicate}')

    def or_(self, predicate):
        return Predicate(f'{self.expression} or {predicate}')

    @property
    def not_(self):
        return Predicate(not_=True)
