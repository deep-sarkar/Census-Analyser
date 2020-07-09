class BaseException(Exception):
    pass

class FileIsNotCSVTypeException(BaseException):
    pass

class FileNotFoundException(BaseException):
    pass

class EmptyFileException(BaseException):
    pass