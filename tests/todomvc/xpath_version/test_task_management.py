from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from selene_intro.common import x


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    s('//*[@id="new-todo"]').type('a').press_enter()
    s('//*[@id="new-todo"]').type('b').press_enter()
    s('//*[@id="new-todo"]').type('c').press_enter()
    ss('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))

    s('//*[@id="todo-list"]//li[.//text()="b"]//*[' + x.has_css_class('toggle') + ']')\
        .click()
    ss('//*[@id="todo-list"]//li[' + x.has_css_class('completed') + ']')\
        .should(have.exact_texts('b'))
    ss('//*[@id="todo-list"]//li[' + x.has_no_css_class('completed') + ']')\
        .should(have.exact_texts('a', 'c'))
