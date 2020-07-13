class BaseException(Exception):
    pass

class FileIsNotCSVTypeException(BaseException):
    pass

class InvalidDelimiterException(BaseException):
    pass

class EmptyFileException(BaseException):
    pass

