from selene import have
from selene.support.shared import browser


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list li').should(have.exact_texts('a', 'b', 'c'))

    browser.element('#todo-list li:nth-child(2) .toggle').click()
    browser.element('#todo-list li.completed').should(have.text('b'))
    browser.all('#todo-list li:not(.completed)')\
        .should(have.exact_texts('a', 'c'))
