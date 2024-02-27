from vertex import *

def readFileIntoList(filename):
    fileLines = [];

    # read the file line by line and store in list
    file = open(filename, "r");

    for line in file:
        fileLines.append(line.strip('\n'))

    return fileLines;

def makeVertex(vertexInfo, vertexName):
    vertex = Vertex(vertexName, vertexInfo)
    vertex.setInfo(vertexInfo)

    return vertex


def execute(filename):
    fileLines = readFileIntoList(filename)

    # vertices storage start here
    previousVertName = None

    vertices = []
    vertexInfo = []
    newVertexFound = False

    # for each new vertex line create a new vertex object
    for line in fileLines:
        # get vertex name
        vertexName = line[0:line.index(',')]

        if(vertexName != previousVertName or (previousVertName is None)): # new vertex found

            if len(vertexInfo) != 0: # if it is not the first vertex
                vertex = makeVertex(vertexInfo, vertexName)

                vertices.append(vertex)

            newVertexFound = True
            vertexInfo.append(line) # append the first line

        if not newVertexFound: # append remaining lines
            vertexInfo.append(line)

        newVertexFound = False

        previousVertName = vertexName






