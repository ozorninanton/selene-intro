class Predicate:
    def __init__(self, as_not=False):
        self.__as_not = as_not

    def id(self, value):
        return self.__apply_not_(f'@id="{value}"')

    def descendant_with_text(self, value):
        return self.__apply_not_(f'.//text()="{value}"')

    def css_class(self, value):
        return self.__apply_not_(
            f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'
        )

    def __apply_not_(self, expression):
        if self.__as_not:
            return f"not({expression})"
        else:
            return expression


class PredicateProxy(Predicate):
    @property
    def not_(self):
        return Predicate(as_not=True)
