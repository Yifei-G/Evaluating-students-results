class StudentsDataException(Exception):

    def __init__(self, fileName, errorMessage):
        Exception.__init__(self, errorMessage)
        self.fileName = fileName


class BadLine(StudentsDataException):
    # put your code here
    def __init__(self,fileName,line,errorMessage):
        StudentsDataException.__init__(self,fileName,errorMessage)
        self.line = line


class FileEmpty(StudentsDataException):
    # put your code here

    def __init__(self, fileName, errorMessage):
        StudentsDataException.__init__(self, fileName, errorMessage)
