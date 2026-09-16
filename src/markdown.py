'''
All the functions in this file convert markdown syntax into html.
Implementing these functions will give you practice learning the
correct markdown syntax.
'''


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('<i>This is italic!</i> This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('<i>This is italic!</i>')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is <i>italic</i>!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    >>> compile_italic_underscore('<i>a</i> and <i>b</i>')
    '<i>a</i> and <i>b</i>'
    >>> compile_italic_underscore('<i>a</i> and _b')
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''
    return line


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('<b>This is bold!</b> This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('<b>This is bold!</b>')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is <b>bold</b>!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    >>> compile_bold_stars('<b>a</b> <b>b</b>')
    '<b>a</b> <b>b</b>'
    >>> compile_bold_stars('a * b * c')
    'a * b * c'
    >>> compile_bold_stars('***')
    '***'
    '''
    return line


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because
    they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily 
    find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage]
    (https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a> 
    href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage]
    (https://github.com/mikeizbicki/cmc-csci040)')
    '<a> 
    href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage] 
    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage] <a>
    (https://github.com/mikeizbicki/cmc-csci040)>course webpage</a>'
    >>> compile_links('this is wrong: 
        [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage]<a> 
    (https://github.com/mikeizbicki/cmc-csci040'>course webpage</a>'
    >>> compile_links('[a](1) and [b](2)')
    '<a> href="1">a</a> and <a> href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a> href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''
    return line
