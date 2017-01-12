# -*- coding: utf-8 -*-

import click
from syntaxsemanticanalysis import download


@click.command()
@click.option('--dataset',default='ecco-tcp')
def main(dataset):
    """Console script for syntaxsemanticanalysis"""
    download()


if __name__ == "__main__":
    main()
