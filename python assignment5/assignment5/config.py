""" submodule of io_utils.py and get_gene_level_information.py """

_DIRECTORY_FOR_UNIGENE = "/Users/nithyasarabudla/Downloads/assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    """ returns the variable _DIRECTORY_FOR_UNIGENE.
    and this is the path to the data on my system"""
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """returns the variable _FILE_ENDING_FOR_UNIGENE
    and this is the extension for the files  """
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts():
    """returns a dictionary of the hosts.
    This function will be a dictionary for the mapping, used to map common names with scientific names."""
    bos_taurus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_keywords = {

        "bos taurus": bos_taurus,
        "bos_taurus": bos_taurus,
        "cow": bos_taurus,
        "cows": bos_taurus,


        "homo sapiens": homo_sapiens,
        "homo_sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,


        "equus caballus": equus_caballus,
        "equus_caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,


        "mus musculus": mus_musculus,
        "mus_musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,


        "ovis aries": ovis_aries,
        "ovis_aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,


        "rattus norvegicus": rattus_norvegicus,
        "rattus_norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus,

    }
    return host_keywords


def get_error_string_4_exception_type(file: str) -> None:
    """
    Print the invalid argument message for FileNotFoundError
    @param file: The fh_in name

    """
    print(f"Could not create the directory (invalid argument): {file}")
