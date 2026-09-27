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
    parts = line.split('_')

    if len(parts) == 1:
        return line

    num_pairs = (len(parts) - 1) // 2

    result = parts[0]
    i = 1
    while i <= num_pairs * 2:
        result += '<i>' + parts[i] + '</i>' + parts[i + 1]
        i += 2

    if len(parts) % 2 == 0:
        result += '_' + parts[-1]

    return result


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
    parts = line.split('**')

    if len(parts) == 1:
        return line

    num_pairs = (len(parts) - 1) // 2

    result = parts[0]
    i = 1
    while i <= num_pairs * 2:
        result += '<b>' + parts[i] + '</b>' + parts[i + 1]
        i += 2

    if len(parts) % 2 == 0:
        result += '**' + parts[-1]

    return result


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because
    they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily
    find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://x.co/course)!')
    'Click on the <a href="https://x.co/course">course webpage</a>!'
    >>> compile_links('[course webpage](https://x.co/course)')
    '<a href="https://x.co/course">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage](https://x.co/course)')
    'this is wrong:[course webpage]<a>(https://x.co/course)>course webpage</a>'
    >>> compile_links('this is wrong:[course webpage](https://x.co/course')
    'this is wrong:[course webpage]<a>(https://x.co/course'>course webpage</a>'
    >>> compile_links('[a](1) and [b](2)')
    '<a> href="1">a</a> and <a> href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a> href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''
    result = ''
    i = 0
    while True:
        start = line.find('[', i)
        if start == -1:
            result += line[i:]
            break

        end_bracket = line.find(']', start + 1)
        if end_bracket == -1:
            result += line[i:]
            break

        next_char_is_paren = (
            end_bracket + 1 < len(line)
            and line[end_bracket + 1] == '('
        )
        if not next_char_is_paren:
            result += line[i:end_bracket + 1]
            i = end_bracket + 1
            continue

        end_paren = line.find(')', end_bracket + 2)
        if end_paren == -1:
            result += line[i:]
            break

        text = line[start + 1:end_bracket]
        url = line[end_bracket + 2:end_paren]
        result += line[i:start] + '<a href="' + url + '">' + text + '</a>'
        i = end_paren + 1

    return result
