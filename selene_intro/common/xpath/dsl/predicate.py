def id(value):
    return f'@id="{value}"'


def descendant_with_text(value):
    return f'.//text()="{value}"'


def css_class(value):
    return f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'


class __Not:
    @classmethod
    def id(cls, value):
        return f'not({id(value)})'

    @classmethod
    def descendant_with_text(cls, value):
        return f'not({descendant_with_text(value)})'

    @classmethod
    def css_class(cls, value):
        return f'not({css_class(value)})'


not_ = __Not
