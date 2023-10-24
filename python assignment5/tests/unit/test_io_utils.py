"""Test suite for test_io_utils.py"""
import os
import pytest
import get_gene_level_information
from assignment5.io_utils import get_filehandle

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_filehandle_for_OSError
# " doesn't conform to snake_case naming style"
# pylint: disable=C0103
FILE_TO_TEST = "test.txt"


def test_update_host_name():
    # The argument that you need to pass to the function:
    argument_to_function = 'cow'
    # The correct answer that you expect the function to return:
    correct_expected_answer = 'Bos_taurus'
    # The actual answer returned by the function:
    actual_answer = get_gene_level_information.update_host_name(argument_to_function)
    # The error message to be printed if the output is not correct:
    error_message = "Updated host name is not correct"
    # Check if the actual answer is the same as the expected answer, if not print error message
    assert actual_answer == correct_expected_answer, error_message


def test_data_for_gene_file():
    gene_file_name = '/Users/nithyasarabudla/Downloads/assignment5_data/Homo_sapiens/EXD1.unigene'
    correct_tissue_list = ["adult", "brain", "muscle", "normal", "testis"]
    predicted_tissue_list = get_gene_level_information.get_data_for_gene_file(gene_file_name)
    error_message = "No Sorted tissue list found"
    assert correct_tissue_list == predicted_tissue_list, error_message


def _create_test_file(file):
    # not actually run, they are just helper functions for the test script
    # create a test fh_in
    open(file, "w").close()


def test_existing_get_filehandle_4_reading():
    # does it open a fh_in for reading
    # create a test fh_in
    _create_test_file(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_4_writing():
    # does it open a fh_in for writing
    # test
    test = get_filehandle(FILE_TO_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_4_OSError():
    # does it raise on OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_4_ValueError():
    # does it raise on ValueError
    # this should exit
    _create_test_file(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def test_get_filehandle_4_TypeError():
    # does it raise on TypeError
    # this should exit
    _create_test_file(FILE_TO_TEST)
    with pytest.raises(TypeError):
        get_filehandle([], "r")
    os.remove(FILE_TO_TEST)
