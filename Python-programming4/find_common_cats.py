"""
counts how many genes are in each category based on data from the chr21_genes.txt file.
The program prints the results so the categories are arranged in ascending order to an output file
"""

import argparse
from collections import Counter
from assignment4 import io_utils


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence ')

    parser.add_argument('-i1',
                        '--infile1',
                        dest='infile1',
                        type=str,
                        help='Path to the gene description file to open',
                        required=True)

    parser.add_argument('-i2',
                        '--infile2',
                        dest='infile2',
                        type=str,
                        help='Path to the gene category to open',
                        required=True)

    return parser.parse_args()


def parsed_category_data(category_data):
    """

    :param category_data: file containing the category and description information
    :return: dictionary of dictionary of categories and information (count, description)
    """
    category_dic = {}
    for line in category_data:
        category, description = line.split('\t')
        info_dict = {
            'count': 0,
            'description': description
        }

        category = float(category)
        category_dic[category] = info_dict
    return category_dic


def get_categories_from_gene_data(gene_data):
    """

    :param gene_data: file containing the gene data
    :return: list of categories
    """
    gene_data = gene_data[1:]
    category_list = []
    for line in gene_data:
        category = line.split('\t')[-1]
        category = (category.strip('\n'))
        try:
            category = float(category)
        except ValueError:
            continue
        category_list.append(category)
    return category_list


def generate_category_file_data(category_data, category_counts):
    """

    :param category_data: data from category file
    :param category_counts: counts of categories
    :return:The file containing categories along with the description and occurences
    """
    category_sorted_list = sorted(category_data.keys())
    category_file_data = []
    category_file_data.append('Category\tOccurrence\tDescription\n')
    for category in category_sorted_list:
        category_info = category_data[category]
        category_count = category_counts[category]
        line_data = f'{category}\t{category_count}\t{category_info["description"]}'
        category_file_data.append(line_data)
    return category_file_data


def main():
    """

    :return: the main function
    """
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    gene_file_obj = io_utils.get_filehandle(infile1, 'r')
    category_file_obj = io_utils.get_filehandle(infile2, 'r')
    gene_data = gene_file_obj.readlines()
    category_data = category_file_obj.readlines()

    category_data_parsed = parsed_category_data(category_data)
    category_list = get_categories_from_gene_data(gene_data)
    category_count = Counter(category_list)

    file_data = generate_category_file_data(category_data_parsed, category_count)
    category_file_object = io_utils.get_filehandle('OUTPUT/categories.txt', 'w')

    category_file_object.writelines(file_data)
    category_file_object.close()


if __name__ == '__main__':
    main()
