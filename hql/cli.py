import click
import hql.query as query


# @click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.command()
@click.argument('url', required=True)
def main(url):
    """Query HTML files."""
    query.main(url)
