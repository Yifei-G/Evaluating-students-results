from os import strerror
from error import StudentsDataException, BadLine, FileEmpty

studentData = {}


def validateName(firstName, lastName):
    fullName = firstName + lastName
    if fullName.isalpha():
        return True
    else:
        raise BadLine(fileName, fullName,
                      "The name is not in the correct format!")


def validateScore(value):
    try:
        float(value)
        return True
    except ValueError:
        raise BadLine(fileName, value,
                      "The score is not in the correct format!")


def processFile(data):
    studentRecords = data.replace("\n", "").split("\t")
    if validateName(studentRecords[0], studentRecords[1]) and validateScore(studentRecords[2]):
        fullName = studentRecords[0] + " " + studentRecords[1]
        score = float(studentRecords[2])
        if fullName in studentData:
            studentData[fullName] += score
        else:
            studentData[fullName] = score


fileName = input("Please enter the file name:")
if fileName != "result.txt":
    raise StudentsDataException(
        fileName, "Can't find the file in the directory!")
try:
    stream = open(fileName, "rt")
    line = stream.readline()
    if line == "":
        raise FileEmpty(fileName, "This file is empty!")
    while line != "":
        processFile(line)
        line = stream.readline()
        
    for fullNmame, score in studentData.items():
        print(fullNmame, "    ", score)
    stream.close()

except FileEmpty as e:
    print(e)

except BadLine as e:
    print(e, ":", e.line)

except StudentsDataException as e:
    print(e, ":", e.fileName)
