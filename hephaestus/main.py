import click

from hephaestus import __version__
from hephaestus.vocab.cui import Cui


@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Will print verbose messages.")
@click.option('--num', '-n', multiple=False, default=3,
              help='Top N')
@click.option('--cui', '-c', multiple=True, default='',
              help='Cuis as input')
@click.option('--cdm', '-d', multiple=True, default='',
              help='CDM Concepts as input')
@click.option('--fun', '-f', multiple=True, default='',
              help='Functions to execute')
def cli(verbose, num, cui, cdm, fun):
    if verbose:
        print("verbose")
    if 'similar' in fun:
        if len(cdm) > 0:
            similar_cdm(cdm, num)


def similar_cdm(concepts, num):
    c = Cui()
    similar_concepts = []
    c.concept_id = concepts
    codes = c.similar_concepts(num)
    for code in codes:
        similar_concepts.append(code[1])
    click.echo(similar_concepts)


def main_routine():
    click.echo("_________________________________________")
    click.echo("Hephaestus v" + __version__)
    cli()  # run the main function


if __name__ == '__main__':
    main_routine()
