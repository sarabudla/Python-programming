"""
File: nt_fasta_stats.py

This program will open the file and generate two files
we will get to know the Number Accession A's G's C's T's N's
length of the sequence GC percent of the entire sequence


Command for executing the program:

python3 secondary_structure_splitter.py --infile ss.txt
"""

# importing libraries
import sys
import argparse


def get_cli_args():
    """
    Returning parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to generate nucleotide statistics')
    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to the file to open',
                        required=True)
    parser.add_argument('-o', '--outfile', dest='outfile',
                        type=str, help='Pathlist_headers, list_seqs,'
                                       ' fh_out to the file to open',
                        required=True)
    return parser.parse_args()


def main():
    """Business Logic"""
    # getting argument through command line
    args = get_cli_args()
    infile = args.infile
    outfile = args.outfile
    fh_in = get_filehandle(infile, 'r')
    fh_out = get_filehandle(outfile, 'w')
    fh_out.write("Number\t Accession\t    A's\t    G's\t    C's\t   "
                 " T's\t    N's\t    Length\t    GC%")
    list_headers, list_seqs = get_fasta_lists(fh_in)
    output_seq_statistics(list_headers, list_seqs, fh_out)


def get_filehandle(infile, mode):
    """get the file handle using try and except"""
    try:
        file_handle = open(infile, mode=mode)
        return file_handle
    # this command except OSError as error
    except OSError as error:
        print('file cannot be opened', infile)
        raise error
    # this command except ValueError as error
    except ValueError as error:
        print('wrong opening mode')
        raise error

# Defining the function to get sequence and header
# one-to-one correspondence to the data in the lists


def get_fasta_lists(fh_in):
    """Return header lists and sequence list"""
    list_headers = []
    list_seqs = []
    lines = fh_in.readlines()
    for index, line in enumerate(lines):
        # use .rstrip to get rid of the empty space and \n at the end of str
        line = line.rstrip()
        if line.startswith('>'):
            header_line = line
            list_headers.append(header_line)
            s_index = index + 1
            sequence = ''
            while s_index < len(lines) and not lines[s_index].startswith('>'):
                # here command .replace
                # get rid of the /n at the end of str
                sequence += lines[s_index].replace("\n", "")
                s_index += 1
            if sequence != '':
                list_seqs.append(sequence)
            else:
                continue
    if _verify_lists(list_headers, list_seqs):
        # print(list_headers)
        # print(list_seqs
        return list_headers, list_seqs
    return None


def _verify_lists(list_headers, list_seqs):
    """check if the size of header list and seq list are equal"""
    if len(list_headers) != len(list_seqs):
        sys.exit("the size of the sequence and "
                 "the header lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def output_seq_statistics(list_headers, list_seqs, fh_out):
    "Calculating the sequence statistics"
    count = 0
    for i in range(len(list_headers)):
        count += 1
        headers = str(list_headers[i])
        accession_number = _get_ncbi_accession(headers)
        nucleotide_a = _get_num_nucleotides('A', list_seqs[i])
        nucleotide_g = _get_num_nucleotides('G', list_seqs[i])
        nucleotide_c = _get_num_nucleotides('C', list_seqs[i])
        nucleotide_t = _get_num_nucleotides('T', list_seqs[i])
        nucleotide_n = _get_num_nucleotides('N', list_seqs[i])
        length = len(list_seqs[i])
        percent_gc = round((nucleotide_g + nucleotide_c)/length*100, 1)
        fh_out.write("\n" + str(count) + "\t\t" + str(accession_number)
                     + "\t\t" + str(nucleotide_a) + "\t\t" + str(nucleotide_g)
                     + "\t\t" + str(nucleotide_c) + "\t\t" + str(nucleotide_t)
                     + "\t\t" + str(nucleotide_n) + "\t\t" + str(length)
                     + "\t\t" + str(percent_gc))


def _get_ncbi_accession(headers):
    accession_string = headers.split(" ")[0]
    return accession_string


def _get_num_nucleotides(nucleotides, list_seqs):
    count = 0
    for nucleotide in list_seqs:
        count += nucleotide.count(nucleotides)
    return count


if __name__ == '__main__':
    main()
