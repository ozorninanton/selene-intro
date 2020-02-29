def by_class(class_name):
    return F'.//*[contains(concat(" ", normalize-space(@class), " "), " {class_name} ")]'


def by_id(xpath):
    return F'//*[@id="{xpath}"]'


def list_items(list, item):
    return F'{list}//{item}'


def list_item_by_class(list, item, class_name):
    return F'{list_items(list, item)}' \
           F'[contains(concat(" ", normalize-space(@class), " "), " {class_name} ")]'


def list_item_not_by_class(list, item, class_name):
    return F'{list_items(list, item)}' \
           F'[not(contains(concat(" ", normalize-space(@class), " "), " {class_name} "))]'


def list_item_by_text(list, item, text):
    return F'{list_items(list, item)}[.//text()="{text}"]'
