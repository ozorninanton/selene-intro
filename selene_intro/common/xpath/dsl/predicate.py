def id(value):
    return f'@id="{value}"'


def descendant_with_text(value):
    return f'.//text()="{value}"'


def css_class(value):
    return f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'


def not_(predicate):
    return f'not({predicate})'
