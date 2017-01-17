# -*- coding: utf-8 -*-

import click
try:
    import syntaxsemanticanalysis.syntaxsemanticanalysis as ssa
    import syntaxsemanticanalysis.tcp_hdr2csv as sshdr
except ImportError:
    import syntaxsemanticanalysis as ssa
    import tcp_hdr2csv as sshdr

@click.command()
@click.option('--dataset',default='ecco-tcp')
def main(dataset):
    """Console script for syntaxsemanticanalysis"""
    ssa.main()

@click.command()
@click.option('--filename')
def readXML(filename):
    sshdr.proc()


if __name__ == "__main__":
    main()
