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
    
    for i in range(1, len(vertices) + 1):
        verticesNames.append(i)
        
    return verticesNames

def getVerticesBefore(vertexToCheck, perm):
    verticesBefore = []
    for vertex in perm:
        if vertex != int(vertexToCheck.name):
             verticesBefore.append(str(vertex))
        else:
            break
        
    return verticesBefore

def appendExactlyEqualParentSets(parentSets, verticesBefore, vertex):
    for key in vertex.info:
        if vertex.info[key][0] == verticesBefore:
            parentSets.append(vertex.info[key])
            
def appendOneMatchingParentSet(parentSets, vertexToMatch, vertex):
    for key in vertex.info:
        if vertex.info[key][0] == vertexToMatch:
            parentSets.append(vertex.info[key])

def getConsistentParentSets(perm, vertexIndex, startIndex):
    vertex = vertices[vertexIndex]
    parentSets = []
    
    parentSets.append(vertex.info[1])
    
    if startIndex: # first vertex in the permutation
        return parentSets
        
    else:
        verticesBefore = getVerticesBefore(vertex, perm)
        
    # for the vertices before, check matching parent sets
    
    appendExactlyEqualParentSets(parentSets, verticesBefore, vertex)
    
    if len(verticesBefore) != 1:
        for vertexToMatch in verticesBefore:
            appendOneMatchingParentSet(parentSets, list(vertexToMatch), vertex)
        
    return parentSets

def getCostOfPerm(perm): # e.g. 0 1 2 3 4
    
    cost = 0
    i = 0
    
    # for every vertex get its consistent parent set
    for vertex in perm:
        min = float('inf')
        consistentParentSets = getConsistentParentSets(perm, vertex - 1, i == 0)
        i += 1
        
        # get min-cost parent set 
        for parentSet in consistentParentSets:
            if float(parentSet[1]) < min:
                min = float(parentSet[1])
                
        cost += min
        
    return cost
        

def getCostAllPerm(allPerm):
    costs = []
    
    for perm in allPerm:
        costs.append(getCostOfPerm(perm))
        
    return costs
    
def execute(filename):
    fileLines = readFileIntoList(filename)

    global vertices
    vertices = getVertices(fileLines) 
    
    verticesNames = getVerticesNames(vertices)
    
    # get all permutations
    
    allPerm = list(itertools.permutations(verticesNames))    
    
    # get cost of all permutations
    
    allPermCosts = getCostAllPerm(allPerm)

    
    
    








