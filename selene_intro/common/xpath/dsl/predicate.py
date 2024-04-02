class Predicate:
    def __init__(self, not_=False):
        self.__not = not_

    def id(self, value):
        return self.__apply_not_(f'@id="{value}"')

    def descendant_with_text(self, value):
        return self.__apply_not_(f'.//text()="{value}"')

    def css_class(self, value):
        return self.__apply_not_(
            f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'
        )

    def __apply_not_(self, expression):
        if self.__not:
            return f"not({expression})"
        else:
            return expression

    @property
    def not_(self):
        return Predicate(not_=True)
