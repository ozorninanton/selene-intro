def has_css_class(value):
    return f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'


def has_not_css_class(value):
    return f'not({has_css_class(value)})'
