"""
intersecting common genes in two different gene files in an ascending order
"""
import argparse
from assignment4 import io_utils


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description='Provide two gene list (ignore header line), find intersection')

    parser.add_argument('-i1',
                        '--infile1',
                        dest='infile1',
                        type=str,
                        help='Gene list 1 to open',
                        required=True)

    parser.add_argument('-i2',
                        '--infile2',
                        dest='infile2',
                        type=str,
                        help='Gene list 2 to open',
                        required=True)

    return parser.parse_args()


def parse_chr21_gene_data(chr21_gene_data):
    """
    :param chr21_gene_data: file containing gene data
    :return: converting gene data into list
    """
    chr21_gene_data = chr21_gene_data[1:]
    chr21_gene_list = []
    for line in chr21_gene_data:
        symbol = line.split('\t')[0]
        chr21_gene_list.append(symbol)
    return chr21_gene_list


def parse_hugo_gene_data(hugo_gene_data):
    """

    :param hugo_gene_data: file containing hugo gene data
    :return: converting gene file 2 into list
    """
    hugo_gene_data = hugo_gene_data[1:]
    hugo_gene_list = []
    for line in hugo_gene_data:
        symbol = line.split('\t')[0]
        hugo_gene_list.append(symbol)
    return hugo_gene_list


def get_intersection_gene_data(chr21_data, hugo_data):
    """

    :param chr21_data: file containing chr21_gene data
    :param hugo_data: file containing hugo_gene_data
    :return: intersection of two data files
    """
    intersection_list = list(set(chr21_data) & set(hugo_data))
    return intersection_list


def generate_gene_intersection_data(intersection_data):
    """

    :param intersection_data: intersection data of two files
    :return: list to the intersection data to be written to the file
    """
    intersection_file_data = [gene + '\n' for gene in intersection_data]
    return intersection_file_data


def main():
    """

    :return: the main function
    """
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    chr21_gene_obj = io_utils.get_filehandle(infile1, 'r')
    hugo_gene_obj = io_utils.get_filehandle(infile2, 'r')
    gene_data_file1 = chr21_gene_obj.readlines()
    gene_data_file2 = hugo_gene_obj.readlines()

    chr21_genes = parse_chr21_gene_data(gene_data_file1)
    hugo_genes = parse_hugo_gene_data(gene_data_file2)

    chr21_gene_count = len(set(chr21_genes))
    hugo_gene_count = len(set(hugo_genes))
    print(f'Number of unique gene names in chr21_genes.txt: {chr21_gene_count}')
    print(f'Number of unique gene names in hugo_genes.txt: {hugo_gene_count}')

    intersection_data = get_intersection_gene_data(chr21_genes, hugo_genes)
    intersection_data = sorted(intersection_data)
    intersection_data_count = len(intersection_data)
    print(f'Number of common gene symbols found: {intersection_data_count}')

    intersection_file_object = io_utils.get_filehandle('OUTPUT/intersection_output.txt', 'w')
    intersection_file_data = generate_gene_intersection_data(intersection_data)
    intersection_file_object.writelines(intersection_file_data)
    intersection_file_object.close()

    print('Output stored in OUTPUT/intersection_output.txt')


if __name__ == '__main__':
    main()
