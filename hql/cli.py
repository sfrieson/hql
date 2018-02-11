import click


# @click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
# @click.argument('name', default='world', required=False)
@click.group()
def main():
    """Query HTML files."""
    pass

@click.command()
def something():
    """Do something."""
    click.echo('You got something to happen.')

@click.command()
def something_else():
    """Do something else."""
    click.echo('You got something else to happen.')

main.add_command(something)
main.add_command(something_else)
