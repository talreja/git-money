import click

@click.command()
@click.argument('issue')
@click.argument('description')
def cli(issue, description):
    print(issue + ' ' + description) 
