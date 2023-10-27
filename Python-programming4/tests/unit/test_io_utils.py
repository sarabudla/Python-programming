"""
tests for secondary_structure_splitter
"""
import pytest
from assignment4.io_utils import get_filehandle


def test_get_filehandle_4_os_error_chr21():
    """
    test to check if system exits when invalid chr file is passed
    :return: None
    """
    with pytest.raises(SystemExit) as some:
        get_filehandle('chr21_genes2.txt', 'r')
    assert isinstance(some.value, SystemExit), "System did not exit"


def test_get_filehandle_4_os_error_hugo():
    """
    test to check if system exits when invalid hugo file is passed
    :return: None
    """
    with pytest.raises(SystemExit) as some:
        get_filehandle('hugo_genes2.txt', 'r')
    assert isinstance(some.value, SystemExit), "System did not exit"


def test_get_filehandle_4_value_error_chr21():
    """
    test to check if system exits when invalid chr file is passed
    :return: None
    """
    with pytest.raises(SystemExit) as some:
        get_filehandle('chr21_genes2.txt', 'r')
    assert isinstance(some.value, SystemExit), "System did not exit"


def test_get_filehandle_4_value_error_hugo():
    """
    test to check if system exits when invalid hugo file is passed
    :return: None
    """
    with pytest.raises(SystemExit) as some:
        get_filehandle('hugo_genes2.txt', 'r')
    assert isinstance(some.value, SystemExit), "System did not exit"


def test_file_opens_successfully_mode_r_chr21():  # mode w, or pass other files
    """
    test to check if chr21 file opens successfully in read mode
    :return: None
    """
    f_actual = open('chr21_genes.txt', 'r', encoding="UTF-8")
    f_function = get_filehandle('chr21_genes.txt', 'r')
    assert f_actual.name == f_function.name
    assert f_actual.mode == f_function.mode


def test_file_opens_successfully_mode_r_hugo():  # mode w, or pass other files
    """
    test to check if hugo file opens successfully in read mode
    :return: None
    """
    f_actual = open('hugo_genes.txt', 'r', encoding="UTF-8")
    f_function = get_filehandle('hugo_genes.txt', 'r')
    assert f_actual.name == f_function.name
    assert f_actual.mode == f_function.mode


def test_file_opens_successfully_mode_r_categories():  # mode w, or pass other files
    """
    test to check if categories file opens successfully in read mode
    :return: None
    """
    f_actual = open('categories.txt', 'w', encoding="UTF-8")
    f_function = get_filehandle('categories.txt', 'w')
    assert f_actual.name == f_function.name
    assert f_actual.mode == f_function.mode


def test_file_opens_successfully_mode_r_intersection():  # mode w, or pass other files
    """
    test to check if intersection file opens successfully in read mode
    :return: None
    """
    f_actual = open('intersection_output.txt', 'w', encoding="UTF-8")
    f_function = get_filehandle('intersection_output.txt', 'w')
    assert f_actual.name == f_function.name
    assert f_actual.mode == f_function.mode
