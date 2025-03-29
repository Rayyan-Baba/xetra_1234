"""Custom Exceptions"""

class WrongFormatException(Exception):
    """
    WrongFormatExeption class

    Exception that can be raised when the format type
    given as parameter is not supported.
    """

class WrongMetaFileException(Exception):
    """
    WrongMetaFileExeption class 

    Exception that can be raised when the meta file 
    format is not correct.
    """