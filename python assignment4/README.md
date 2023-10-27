
# Overview

## input files 
- The `chr21_genes.txt` file lists genes from human chromosome 21
- The `HUGO_genes.txt` file lists all human genes having official symbol approved by the HUGO gene nomenclature committee

## gene_names_from_chr21.py
- gene_names_from_chr21.py asks the user to enter a gene symbol
- prints the description for that gene based on data from the chr21_genes.txt file.

## find_common_cats.py
- counts how many genes are in each category based on data from the chr21_genes.txt file.
- The program prints the results so the categories are arranged in ascending order to an output file `categories.txt`

## intersection_of_gene_names.py
- intersecting common genes in two different gene files in an ascending order
- Printing the ascending order genes to output file `intersection_output.txt`
