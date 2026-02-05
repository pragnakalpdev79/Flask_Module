import click

def register(app):
    @app.cli.command('mycmd')
    def mycmd():
        click.echo("Test")