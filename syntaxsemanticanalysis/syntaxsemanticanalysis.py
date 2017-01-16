# -*- coding: utf-8 -*-
from __future__ import print_function
import sys, os
import shutil
from zipfile import ZipFile
import re, requests
from bs4 import BeautifulSoup
try:
    import urllib.request as ul
except ImportError:
    import urllib as ul


directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
dataset = "ecco-tcp"


def unzip_ecco_tcp_xmls(origin_directory, destination_directory):
    """
    Create, if doesn't exist, the destination_directory and unzip all zip files contained in origin_directory.
    If the origin_directory doesn't exist, an exception is raised.
    :param origin_directory: The directory's path where ECCO-TCP zip files are stored
    :param destination_directory: The directory's path where the ECCO-TCP dataset will be unzipped
    :return: None
    """
    if not files_actually_unzipped(origin_directory, destination_directory):
            for file in os.listdir(origin_directory):
                if file.endswith(".zip"):
                    ZipFile(os.path.join(origin_directory, file)).extractall(destination_directory)


def files_actually_unzipped(origin_directory, destination_directory):
    """
    Verifies if the origin_directory with zipped files are actually unzipped. If files are unzipped, return True.
    Returns False otherwise. If the origin_directory doesn't exist an IOError is raised.
    :param origin_directory: The directory's path where ECCO-TCP zip files are stored
    :param destination_directory: The directory's path where the ECCO-TCP dataset will be unzipped
    :return: True or False
    """
    names = []
    if not os.path.exists(origin_directory):
        raise IOError("The dataset directory doesn't exist")
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
    for file in os.listdir(origin_directory):
        if file.endswith(".zip"):
            names += ZipFile(os.path.join(origin_directory, file)).namelist()
    other_names = os.listdir(destination_directory)
    return len(set(names) & set(other_names)) == len(set(names))


def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(barLength * iteration // total)
    bar = fill * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

def download(datasetname = "ecco-tcp", dataseturl = "http://www.lib.umich.edu/tcp/docs/texts/ecco/"):
    if not os.path.exists(os.path.join(directory,dataset)):
        os.makedirs(os.path.join(directory,dataset))
    for url, filename in get_all_data(dataseturl):
        print("Downloading "+filename+":",)
        ul.urlretrieve(url,os.path.join(directory,dataset,filename),reporthook)


def get_all_data(dataseturl):
    soup = BeautifulSoup(requests.get(dataseturl).text, "lxml")
    for a in soup.find('table').find_all('a'):
        link = a['href']
        if re.match(r'^xml.*\.zip', link) or 'headers.ecco.zip' in link:
            yield dataseturl + link, link


def reporthook(blocknum, blocksize, totalsize):
    read = blocknum * blocksize
    total = totalsize // blocksize
    if totalsize > 0:
        percent = read * 100 // totalsize
        printProgress(percent, 100,prefix='Progress:',suffix='Complete', barLength=50)


def main():
    download()
    unzip_ecco_tcp_xmls(os.path.join(directory,dataset),os.path.join(directory,dataset+"_unzipped"))
    shutil.rmtree(os.path.join(directory,dataset))
    shutil.move(os.path.join(directory,dataset+"_unzipped"), os.path.join(directory,dataset))


if __name__ == "__main__":
    main()
