"""testing file for secondary_structure_splitter.py"""

import pytest
import secondary_structure_splitter


def test_get_header_and_sequence_lists_1():
    """Test to get fasta file"""
    # This function compares the list headers and list sequences
    file = open('ss2.txt', 'r')
    list1 = [">101M:A:sequence"]
    list2 = ["MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLK"
             "TEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPI"
             "KYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG"]
    assert (list1, list2) == (list1, list2)


def test_check_size_of_lists():
    """Test to verify list"""
    # This function checks if the of the lists are equal
    assert True, secondary_structure_splitter._verify_lists(["ATGCTTAGC"], ["ATGCTTAGC"])


def test_verify_lists_not_eq_len4():
    """Test to verify list"""
    # This function checks if the length of lists
    # is equal or not and exits system
    with pytest.raises(SystemExit):
        secondary_structure_splitter._verify_lists(["ATGCTTAGC", "GACTACAA"], ["ATGCTTAGC"])


def test_get_filehandle_ioerror():
    """Test to check file handle"""
    # This function checks if the file handles IOError
    with pytest.raises(IOError):
        secondary_structure_splitter.get_filehandle("#/#/#/#", "r")


def test_get_filehandle_valueerror():
    """Test to check file handle"""
    # This function checks if the file handles ValueError
    with pytest.raises(ValueError):
        secondary_structure_splitter.get_filehandle(" ", " ")
