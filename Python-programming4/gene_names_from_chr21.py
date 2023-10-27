"""
gene_names_from_chr21.py asks the user to enter a gene symbol
and then prints the description for that gene based on data from the chr21_genes.txt file.
"""
import argparse
from assignment4 import io_utils


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt, and ask user for a gene name ')

    parser.add_argument('-i',
                        '--infile',
                        dest='infile',
                        type=str,
                        help='Path to file to open',
                        required=True)

    return parser.parse_args()


def parse_gene_data(file_data):
    """
    :param file_data: the data in the text file
    :return: gene dictionary
    """
    file_data = file_data[1:]
    gene_dict = {}
    for line in file_data:
        symbol, description, category = line.split('\t')
        gene_data_dict = {
            'description': description,
            'category': category,
        }
        gene_dict[symbol.lower()] = gene_data_dict
    return gene_dict


def main():
    """

    :return: print statements which has be to written out
    """
    args = get_cli_args()
    infile = args.infile
    gene_file_obj = io_utils.get_filehandle(infile, 'r')
    gene_data = gene_file_obj.readlines()
    gene_data_parsed = parse_gene_data(gene_data)

    while True:
        user_input = input('Enter gene name of interest. Type quit to exit: ')
        user_input_org = user_input
        user_input = user_input.lower()

        if user_input in ('exit', 'quit'):
            print('Thanks for querying the data.')
            break
        if user_input in gene_data_parsed:
            gene_info = gene_data_parsed[user_input]
            description = gene_info['description']
            print(f'{user_input_org} found! Here is the description:\n{description}')
        else:
            print('Not a valid gene name.')

        print()


if __name__ == '__main__':
    main()
