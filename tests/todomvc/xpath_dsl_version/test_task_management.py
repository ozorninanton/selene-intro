from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from selene_intro.common.xpath.dsl import its, x


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    s(x.all().by(its.id('new-todo')).x).type('a').press_enter()
    s(x.all().by(its.id('new-todo')).x).type('b').press_enter()
    s(x.all().by(its.id('new-todo')).x).type('c').press_enter()
    ss(x.all().by(its.id('todo-list')).child('li').x).should(have.exact_texts('a', 'b', 'c'))

    s(x.all().by(its.id('todo-list'))
      .child('li').by(its.descendant_with_text('b'))
      .descendant().by(its.css_class('toggle'))
      .x).click()
    ss(x.all().by(its.id('todo-list'))
       .child('li').by(its.css_class('completed'))
       .x).should(have.exact_texts('b'))
    ss(x.all().by(its.id('todo-list'))
       .child('li').by_not(its.css_class('completed'))
       .x).should(have.exact_texts('a', 'c'))
