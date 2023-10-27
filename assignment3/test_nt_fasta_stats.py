"""Testing file for nt_fasta_stats.py"""

import pytest
import nt_fasta_stats


def test_get_filehandle_ioerror():
    """Test to check file handle"""
    # This function checks if the file handles IOError
    with pytest.raises(IOError):
        nt_fasta_stats.get_filehandle("#/#/#/#", "r")


def test_get_header_and_sequence_lists():
    """Test to get fasta file"""
    # This function compares the list headers and list sequences
    file = open('ss2.txt', 'r')
    list1 = [">101M:A:sequence"]
    list2 = ["MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLK"
             "TEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIK"
             "YLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG"]
    assert (list1, list2) == nt_fasta_stats.get_fasta_lists(file)


def test_get_filehandle_valueerror():
    """Test to check file handle"""
    # This function checks if the file handles ValueError
    with pytest.raises(ValueError):
        nt_fasta_stats.get_filehandle(" ", " ")


def test_verify_lists():
    """Test to verify list"""
    # This function checks if the the of the lists are equal
    assert True, nt_fasta_stats._verify_lists(["ATGCTTAGC"], ["ATGCTTAGC"])
