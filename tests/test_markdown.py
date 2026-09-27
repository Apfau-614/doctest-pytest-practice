'''
Integration tests for the functions in src/markdown.py.

A real markdown compiler applies every rule to the same line of text,
so these tests check that the compilers work together correctly.
'''

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.markdown import (  # noqa: E402
    compile_bold_stars,
    compile_italic_underscore,
    compile_links,
)


def compile_all(line):
    '''
    Apply every markdown compiler to a single line of text.
    '''
    return compile_links(compile_bold_stars(compile_italic_underscore(line)))


def test_plain_text_is_unchanged():
    assert compile_all('just some plain text') == 'just some plain text'


def test_bold_and_italic_together():
    line = '<b>bold</b> and <i>italic</i>'
    assert compile_all(line) == '<b>bold</b> and <i>italic</i>'


def test_link_with_bold_text():
    line = '[<b>click</b>](https://example.com)'
    expected = '<a href="https://example.com"><b>click</b></a>'
    assert compile_all(line) == expected


def test_link_with_italic_text():
    line = '[<i>click</i>](https://example.com)'
    expected = '<a href="https://example.com"><i>click</i></a>'
    assert compile_all(line) == expected


def test_every_feature_on_one_line():
    line = 'See the [docs](https://x.com) for <b>more</b> <i>info</i>.'
    expected = (
        'See the <a href="https://x.com">docs</a> '
        'for <b>more</b> <i>info</i>.'
        )
    assert compile_all(line) == expected


def test_bold_and_italic_order_does_not_matter():
    line = '<b>bold</b> and <i>italic</i>'
    bold_first = compile_italic_underscore(compile_bold_stars(line))
    italic_first = compile_bold_stars(compile_italic_underscore(line))
    assert bold_first == italic_first


def test_compiling_twice_changes_nothing():
    line = 'a [link](url) with <b>bold</b> and <i>italic</i> text'
    once = compile_all(line)
    assert compile_all(once) == once
