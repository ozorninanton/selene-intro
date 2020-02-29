from selene import have
from selene.support.shared import browser

from api.helpers import *


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element(by_id('new-todo')).type('a').press_enter()
    browser.element(by_id('new-todo')).type('b').press_enter()
    browser.element(by_id('new-todo')).type('c').press_enter()
    browser.all(list_items(by_id('todo-list'), 'li')).should(have.exact_texts('a', 'b', 'c'))

    browser.element(list_item_by_text(by_id('todo-list'), 'li', 'b'))\
        .element(by_class('toggle')).click()
    browser.element(list_item_by_class(by_id('todo-list'), 'li', 'completed'))\
        .should(have.exact_text('b'))
    browser.all(list_item_not_by_class(by_id('todo-list'), 'li', 'completed'))\
        .should(have.exact_texts('a', 'c'))
