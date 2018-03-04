from bs4 import BeautifulSoup

"""
SELECT str # what is returned, space separated
[WHERE exp] # how to know which to choose get data from, boolean delimited
[LIMIT bla] # max number to return
[OFFSET num] # max number to return
"""

default_limit = 50
default_offset = 0


def main(query, html):
    global default_limit
    global default_offset
    soup = BeautifulSoup(html, 'html.parser')

    pieces = {
        'SELECT': [],
        'WHERE': [],
        'LIMIT': [],
        'OFFSET': []
    }
    current = ''
    split_query = query.split(' ')

    print(split_query)
    for word in split_query:
        print(word)
        if word.upper() in pieces:
            print('it is a keyword')
            current = word.upper()
        else:
            print('it is an input')
            pieces[current].append(word)

    print(pieces)

    limit = (len(pieces['LIMIT']) and pieces['LIMIT'][0]) or default_limit
    offset = (len(pieces['OFFSET']) and pieces['OFFSET'][0]) or default_offset
    matches = find(soup, pieces['WHERE'])[offset:limit]
    return values(matches, pieces['SELECT'])


"""
Currently supports soup Tag attributes like:
- attrs
- children
- contents
- name
- parent (?)
- text
"""


def find(soup, params):
    if params:
        found = []
        for el in soup.find_all():
            data = select(el, params[0])
            if params[2] == data or params[2] in data:
                found.append(el)
        return found
    else:
        return [el for el in soup.find_all()]


"""
Currently supports the same list of Tag attributes above
"""


def values(matches, params):
    selections = []
    for el in matches:
        row = {}
        for val in params:
            row[val] = select(el, val) or ''
        selections.append(row)

    return selections


attribute_list = ['children', 'contents', 'name', 'parent', 'text']


def select(element, prop):
    if prop in attribute_list:
        return getattr(element, prop)
    else:
        return element.get(prop, '')
