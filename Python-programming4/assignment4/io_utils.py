"""
Utility file
"""
import sys


def get_filehandle(filename, mode):
    """
    Opens the file from its file name based on the specified mode
    :param filename: Name of the file to be opened
    :param mode: mode in which the file needs to be opened (r for read,w for write,etc..)
    :return: returns the file handle if no error otherwise exits
    """
    try:
        file = open(filename, mode, encoding="UTF-8")
    # except OSError:
    #     print("Did you provide a FASTA formatted file?")
    #     sys.exit()
    except ValueError:
        print("Please provide correct opening mode")
        sys.exit()
    except FileNotFoundError:
        print('Did you provide a file?')
        sys.exit()
    return file
