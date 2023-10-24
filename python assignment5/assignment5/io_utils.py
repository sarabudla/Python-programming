"""submodule for get_gene_level_information.py """

import os
import sys


def get_filehandle(file=None, mode=None):
    """
     filehandle : get_filehandle(infile, "r")
      Takes : 2 arguments file name and mode i.e. what is needed to be done with
      this file. This function opens the file based on the mode passed in
      the argument and returns filehandle.
      @param file: The file to open for the mode
      @param mode: They way to open the file, e.g. reading, writing, etc
      @return: filehandle
      """

    try:
        fobj = open(file, mode)
        return fobj
    except FileNotFoundError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise


def is_gene_file_valid(file_name):
    """This function will check to make sure the given file name exists,
    if it does it return True else it will return False"""
    return os.path.exists(file_name)
