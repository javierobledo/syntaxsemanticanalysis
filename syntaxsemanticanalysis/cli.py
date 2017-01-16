# -*- coding: utf-8 -*-

import click
import syntaxsemanticanalysis.syntaxsemanticanalysis
import syntaxsemanticanalysis.tcp_hdr2csv


@click.command()
@click.option('--dataset',default='ecco-tcp')
def main(dataset):
    """Console script for syntaxsemanticanalysis"""
    syntaxsemanticanalysis.syntaxsemanticanalysis.main()

@click.command()
@click.option('--filename')
def readXML(filename):
    syntaxsemanticanalysis.tcp_hdr2csv.proc()


if __name__ == "__main__":
    main()
