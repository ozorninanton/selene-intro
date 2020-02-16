from selene import by, have
from selene.support.shared import browser, config

config.timeout = 6  # browser.config.timeout = 6


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element(by.id('new-todo')).type('a').press_enter()
    browser.element(by.id('new-todo')).type('b').press_enter()
    browser.element(by.id('new-todo')).type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()
    browser.all('#todo-list>li').filtered_by(have.css_class('completed')) \
        .should(have.exact_text('b'))
    browser.all('#todo-list>li').filtered_by(have.no.css_class('completed')) \
        .should(have.exact_texts('a', 'c'))
