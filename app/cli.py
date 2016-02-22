import click
from app.github import github

@click.command()
@click.argument('issue')
@click.argument('description')
def cli(issue, description):
    github.create_issue(issue, description)
    print(issue + ' ' + description) 
