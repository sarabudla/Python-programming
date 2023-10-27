"""
File: secondary_structue_splitter.py

This program will open the file and generate two files
one is protein sequence and other one is secondary structures.

Command for executing the program:

python3 secondary_structure_splitter.py --infile ss.txt
"""

import sys
import argparse


def get_cli_args():
    """
    Returns parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform splitting on'
                    ' sequence and secondary structure ')
    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to the file to open',
                        required=True)
    return parser.parse_args()


def main():
    """Business Logic"""
    # getting argument through command line
    args = get_cli_args()
    infile, mode = args.infile, 'r'
    fh_in = get_filehandle(infile, mode)
    pdb_protein_fh = get_filehandle('pdb_protein.fasta', 'w')
    pdb_ss_fh = get_filehandle('pdb_ss.fasta', 'w')
    list_headers, list_seqs = get_fasta_lists(fh_in)
    seq_count, ss_count = 0, 0
    # parsing the handle to obtain the record
    for i, header in enumerate(list_headers):
        if header.endswith('sequence'):
            pdb_protein_fh.write(header+'\n')
            pdb_protein_fh.write(list_seqs[i]+'\n')
            seq_count += 1
        elif header.endswith('secstr'):
            pdb_ss_fh.write(header+'\n')
            pdb_ss_fh.write(list_seqs[i]+'\n')
            ss_count += 1
    # here this command gives output
    print('Found {} protein sequences' .format(seq_count))
    print('Found {} ss sequences' .format(ss_count))
    # here this command closes the files
    pdb_protein_fh.close()
    pdb_ss_fh.close()


def get_filehandle(infile, mode):
    """getting the file handle"""
    try:
        file_handle = open(infile, mode=mode)
        return file_handle
    except IOError as error:
        print('cannot open', infile)
        raise error
    except ValueError as error:
        print('wrong open mode')
        raise error


def get_fasta_lists(fh_in):
    """Return header lists and sequence list"""
    # creating empty list called list_headers
    list_headers = []
    # creating empty list called list_seqs
    list_seqs = []
    # this command reads every line in the file
    lines = fh_in.readlines()
    # the for loop is used to iterate
    for ind, line in enumerate(lines):
        # here we are removing the empty space
        line = line.rstrip()
        if line.startswith('>'):
            header_line = line
            list_headers.append(header_line)
            s_id = ind + 1
            sequence = ''
            while s_id < len(lines) and not lines[s_id].startswith('>'):
                # by using this command .replace
                # get rid of the /n at the end of str
                sequence += lines[s_id].replace("\n", "")
                s_id += 1
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
    """checking if the size of header list and seq list are equal"""
    if len(list_headers) != len(list_seqs):
        sys.exit("Header and Sequence lists size are different in size \n"
                 "Did you provide a FASTA formatted file?")
    else:
        return True


if __name__ == '__main__':
    main()
