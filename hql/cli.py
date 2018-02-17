import click
import hql.query as query
import re

message_set_url = ('Please set the a url with `url` and '
                   'and query it with `refresh`.')


@click.command()
@click.argument('url', required=False)
def main(url):
    """Query HTML files."""
    response = 'No response yet.\n%s' % message_set_url
    if url:
        response = query.main(url)

    user_input = ''
    while user_input != 'exit':
        user_input = input('> ')

        if user_input == 'help':
            print("""Commands:

exit - to exit
help - You already know this one.
refresh - to requery the current url page
response - to see the HTML response
url - to retrieve and set the current url
            """)
        elif user_input == 'refresh':
            if url:
                response = query.main(url)
            else:
                print("No url is set.\n%s" % message_set_url)
        elif user_input == 'response':
            print(response)
        elif user_input == 'url':
            print(url)
        elif re.match(r'^SELECT', user_input, flags=re.IGNORECASE):
            print(user_input)
