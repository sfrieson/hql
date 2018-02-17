import click
import hql.data as data

import re

message_set_url = ('Please set the a url with `url` and '
                   'and query it with `refresh`.')


@click.command()
@click.argument('url', required=False)
def main(url):
    """Query HTML files."""
    response = 'No response yet.\n%s' % message_set_url
    if url:
        response = data.main(url)

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
                response = data.main(url)
            else:
                print("No url is set.\n%s" % message_set_url)
        elif user_input == 'response':
            print(response)
        elif re.match(r'^URL', user_input, flags=re.IGNORECASE):
            commands = user_input.split(' ')
            command_count = len(commands)
            if command_count == 1:
                print(url)
            elif command_count == 2:
                url = commands[1]
            else:
                print('`url` only accepts 1 argument')
        elif re.match(r'^SELECT', user_input, flags=re.IGNORECASE):
            print(user_input)
