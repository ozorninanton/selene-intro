def id(value):
    return f'*[@id="{value}"]'


def descendant_with_text(value):
    return f'[.//text()="{value}"]'


def css_class(value):
    return f'[contains(concat(" ", normalize-space(@class), " "), " {value} ")]'


def no_css_class(value):
    return f'[not(contains(concat(" ", normalize-space(@class), " "), " {value} "))]'
