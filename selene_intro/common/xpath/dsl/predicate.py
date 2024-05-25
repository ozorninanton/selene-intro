class Predicate:
    def __init__(self, condition=None, not_=False):
        self.__condition = condition
        self.__not = not_

    def __str__(self):
        condition = f'not({self.__condition})' if self.__not else self.__condition
        self.__condition, self.__not = None, False
        return condition

    def id(self, value):
        return Predicate(f'@id="{value}"', self.__not)

    def descendant_with_text(self, value):
        return Predicate(f'.//text()="{value}"', self.__not)

    def css_class(self, value):
        return Predicate(
            f'contains(concat(" ", normalize-space(@class), " "), " {value} ")',
            self.__not
        )

    def and_(self, predicate):
        if self.__condition is None:
            raise Exception('cannot be called while __condition is None')
        return Predicate(f'{self.__condition} and {predicate}')

    def or_(self, predicate):
        if self.__condition is None:
            raise Exception('cannot be called while __condition is None')
        return Predicate(f'{self.__condition} or {predicate}')

    @property
    def not_(self):
        return Predicate(not_=True)
