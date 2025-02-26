# Entry point for cli

import click

from scaffold.generators.module_generator import generate_module
from scaffold.generators.project_generator import generate_project


@click.group()
def cli():
    """Flask Scafifold cli"""
    pass


@cli.command()
@click.argument('project_name')
def create_project(project_name):
    """Scaffolds the projects"""
    generate_project(project_name)
    click.echo(f"Project '{project_name}' created successfully!")


@cli.command()
@click.argument('module_name')
def add_module(module_name):
    """Generate a new module with CRUD endpoints."""
    generate_module(module_name)
    click.echo(f"Module '{module_name}' added successfully!")

if __name__ == '__main__':
    cli()