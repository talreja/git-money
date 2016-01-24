import click

@click.command()
@click.argument('issue')
@click.argument('description')
def cli(issue, description):
    print(issue + ' ' + description) #Dummy function to ensure that this is working. Will feed into broader script.
