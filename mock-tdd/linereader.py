import os


def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad Path!")
    infile = open(filename, "r")
    line = infile.readline()
    return line
