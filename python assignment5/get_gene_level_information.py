"""
File    :get_gene_level_information.py
query the tissue expression for a given gene and species.
"""

import sys
import re
import argparse
from assignment5.config import get_keywords_for_hosts, get_extension_for_unigene, get_directory_for_unigene
from assignment5.io_utils import get_filehandle


def get_cli_args():
    """ CLI options using Python's argparse
     @return: Instance of argparse arguments"""
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')

    parser.add_argument('--host', dest='HOST',
                        help='Name of Host', required=False, default='Human')
    parser.add_argument('-g', '--gene', dest='GENE',
                        help='Name of Gene', required=False, default='TGM1')

    return parser.parse_args()


def update_host_name(host_name):
    """ This function take the host name and checks for the available conversions from common to scientific names
     and return the scientific name.
      This function calls get_keywords_for_hosts to get the dictionary of mapped
      terms from the assignment5.config.py module.
       If the host passed in does not exist then it calls the function
       _print_directories_for_hosts and exit the program."""

    dictionary = get_keywords_for_hosts()
    host_name = host_name.lower()

    if host_name in dictionary:
        return dictionary[host_name]
    else:
        _print_directories_for_hosts()
        return None


def _print_directories_for_hosts():
    """ This function use the get_keywords_for_hosts to get the hosts and
    Prints the list of available Hosts by scientific and common names """

    print('\n\nEither the Host Name you are searching for is not in the database\n\nor If you are trying to use the '
          'scientific name please put the name in double quotes:\n\n"Scientific name"')
    dictionary = get_keywords_for_hosts()
    scientific = set(dictionary.values())
    common = dictionary.keys()

    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name \n")
    for i, scientific_names in enumerate(sorted(scientific)):
        print("  " + str(i + 1) + ".", scientific_names[0].upper() + scientific_names[1:])
    print("\n\nHere is a (non-case sensitive) list of available Hosts by common name \n")
    count = 1
    for common_names in sorted(common):
        if '_' not in common_names:
            print("  " + str(count) + ".", common_names[0].upper() + common_names[1:])
            count += 1
    sys.exit()


def get_data_for_gene_file(gene_file_name):
    """ get_data_for_gene_file opens the file for the host and gene, extracts the list of tissues in which this gene
    is expressed and returns a sorted list of the tissues. """

    fh_in = get_filehandle(gene_file_name, "r")

    for line in fh_in:
        match = re.search(r'EXPRESS(.*)', line)
        if match:
            tissue_string = match.group(1)  # match here is an object. group1
            tissue_list = list(tissue_string.split('|'))
            sorted_tissue_list = [i.strip() for i in tissue_list]
            sorted_tissue_list = sorted(sorted_tissue_list)
            return sorted_tissue_list
    return None


def print_host_to_gene_name_output(host_name, gene_name, sorted_tissue_list):
    """This function prints the tissue expression data for the gene."""
    host_name = ' '.join(host_name.split('_'))
    print(f"\nFound Gene {gene_name} for {host_name} \nIn {host_name}, There are {len(sorted_tissue_list)} tissues "
          f"that {gene_name} is expressed in:\n")
    for i, tissue in enumerate(sorted_tissue_list):
        print("  " + str(i + 1) + ".", tissue[0].upper() + tissue[1:])


def main():
    """
    get cli arguments
    get host and gene from cli arguments
    check if host exists using update_host_name and get the updated name
    get data using get_data_... function
    print data using print_host_...

    :return:
    """
    args = get_cli_args()
    host = args.HOST
    gene = args.GENE
    updated_host = update_host_name(host)
    file = "/".join((get_directory_for_unigene(), updated_host, gene + "." + get_extension_for_unigene()))
    sorted_tissues = get_data_for_gene_file(file)
    print_host_to_gene_name_output(updated_host, gene, sorted_tissues)


if __name__ == '__main__':
    main()
