from selene import have
from selene.support.shared import browser


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()
    browser.all('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))

    browser.element('//*[@id="todo-list"]//li[.//text()="b"]'
                    '//*[contains(concat(" ", normalize-space(@class), " "), " toggle ")]')\
        .click()
    browser.element('//*[@id="todo-list"]'
                    '//li[contains(concat(" ", normalize-space(@class), " "), " completed ")]')\
        .should(have.exact_text('b'))
    browser.all('//*[@id="todo-list"]'
                '//li[not(contains(concat(" ", normalize-space(@class), " "), " completed "))]')\
        .should(have.exact_texts('a', 'c'))
