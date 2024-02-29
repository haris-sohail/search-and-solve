from vertex import *
import itertools

def readFileIntoList(filename):
    fileLines = [];

    # read the file line by line and store in list
    file = open(filename, "r");

    for line in file:
        fileLines.append(line.strip('\n'))

    return fileLines;

def makeVertex(vertexInfo, vertexName):
    vertex = Vertex(vertexName)
    vertex.setInfo(vertexInfo)

    return vertex

def getVertices(fileLines):
    previousVertName = None

    vertices = []
    vertexInfo = []
    newVertexFound = False
    firstVertex = True

    # for each new vertex line create a new vertex object
    for line in fileLines:
        # get vertex name
        vertexName = line[0:line.index(',')]

        if(vertexName != previousVertName or (previousVertName is None)): # new vertex found

            if len(vertexInfo) != 0 or (firstVertex == False): # if it is not the first vertex
                vertex = makeVertex(vertexInfo, previousVertName)
                vertexInfo.clear()

                vertices.append(vertex)

                firstVertex = False

            newVertexFound = True
            vertexInfo.append(line) # append the first line

        if not newVertexFound: # append remaining lines
            vertexInfo.append(line)

        newVertexFound = False

        previousVertName = vertexName

    # append the last vertex
    vertex = makeVertex(vertexInfo, previousVertName)
    vertexInfo.clear()

    vertices.append(vertex)

    return vertices

def getVerticesNames(vertices):
    verticesNames = []
    
    for i in range(0, len(vertices)):
        verticesNames.append(i)
        
    return verticesNames


def execute(filename):
    fileLines = readFileIntoList(filename)

    vertices = getVertices(fileLines) 
    
    verticesNames = getVerticesNames(vertices)
    
    # get all permutations
    
    allPerm = list(itertools.permutations(verticesNames))
    
    
    
    
    








