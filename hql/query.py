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
    for word in split_query:
        if word.upper() in pieces:
            current = word.upper()
        else:
            pieces[current].append(word)

    limit = pieces['LIMIT'][0] or default_limit
    offset = pieces['OFFSET'][0] or default_offset
    matches = find(soup, pieces['WHERE'])[offset:limit]
    return values(matches)


def find(soup, params):
    pass


def values(soup, params):
    pass
