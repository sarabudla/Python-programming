"""Test suite for module config.py"""
from assignment5 import config
from assignment5.config import get_directory_for_unigene
from assignment5.config import get_extension_for_unigene
from assignment5.config import get_error_string_4_exception_type


# ignore all "Missing function or method docstring"
# since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

def test_get_keywords_for_hosts():
    test_file = config.get_keywords_for_hosts()
    assert test_file.get("bos taurus") == "Bos_taurus"
    assert test_file.get("horse") == "Equus_caballus"
    assert test_file.get("rat") == "Rattus_norvegicus"
    assert test_file.get("humans") == "Homo_sapiens"
    assert test_file.get("sheep") == "Ovis_aries"


def test_get_directory_for_unigene():
    actual_answer = get_directory_for_unigene()
    expected_answer = "/Users/nithyasarabudla/Downloads/assignment5_data"
    error_message = "Directory not correct"
    assert expected_answer == actual_answer, error_message


def test_get_extension_for_unigene():
    actual_answer = get_extension_for_unigene()
    expected_answer = "unigene"
    error_message = ""
    assert expected_answer == actual_answer, error_message


def test_get_error_string_4_exception_type(capsys):
    file = 'test_io_utils.py'
    get_error_string_4_exception_type(file)
    actual_answer = capsys.readouterr().out
    expected_answer = f"Could not create the directory (invalid argument): {file}"
    error_message = "Error message was not valid"
    assert actual_answer.strip() == expected_answer, error_message
