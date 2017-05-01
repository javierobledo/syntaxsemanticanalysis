# -*- coding: utf-8 -*-

import click, os
try:
    import syntaxsemanticanalysis.syntaxsemanticanalysis as ssa
    import syntaxsemanticanalysis.tcp_hdr2csv as sshdr
    import syntaxsemanticanalysis.xml2csv as ssxml
except ImportError:
    import syntaxsemanticanalysis as ssa
    import tcp_hdr2csv as sshdr
    import xml2csv as ssxml

@click.command()
@click.option('--dataset',default='ecco-tcp')
def main(dataset):
    """Console script for syntaxsemanticanalysis"""
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
    ssa.main(directory,dataset)
    sshdr.headers_to_csv(directory,dataset)
    ssxml.corpus_to_csv(directory,dataset)

if __name__ == "__main__":
    main()
