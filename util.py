def readFileIntoList(filename):
    fileLines = [];

    # read the file line by line and store in list
    file = open(filename, "r");

    for line in file:
        fileLines.append(line.strip('\n'))
        print(fileLines)

    return fileLines;


def execute(filename):
    fileLines = readFileIntoList(filename);

    

