# Main program
# get_gene_level_information.py
query the tissue expression for a given gene and species.

# update_host_name
This function take the host name and checks for the available conversions from common to scientific names and return the scientific name.
This function calls get_keywords_for_hosts to get the dictionary of mapped terms from the assignment5.config.py module.
If the host passed in does not exist then it calls the function _print_directories_for_hosts and exit the program.

# _print_directories_for_hosts
This function use the get_keywords_for_hosts to get the hosts and Prints the list of available Hosts by scientific and common names

# get_data_for_gene_file
get_data_for_gene_file opens the file for the host and gene, extracts the list of tissues in which this gene is expressed and returns a sorted list of the tissues.

# print_host_to_gene_name_output
This function prints the tissue expression data for the gene.

# Author
Nithya Sarabudla

# Date created 
07-12-2022
