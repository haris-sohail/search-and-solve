import collections

class Vertex:
    def __init__(self, _name = None, _infoDict = None):
        self.name = _name
        if _infoDict is None:
            self.info = collections.defaultdict(list)
        else:
            self.info = _infoDict.copy()

    def setInfo(self, _info):
        info = _info

        # dictionary to store vertexInfo
        for i in range(0, len(info)):
            # extract parent set and cost
            infoArray = info[i].split(',')

            # Remove brackets from parent set
            for j in range(1, len(infoArray) - 1):
                infoArray[j] = infoArray[j].replace('{', '')
                infoArray[j] = infoArray[j].replace('}', '')
                
            # Extract vertices from infoArray
            parentSet = []
            for k in range(1, len(infoArray) - 1):
                parentSet.append(infoArray[k])

            self.info[i + 1].append(parentSet)
            self.info[i + 1].append(infoArray[-1]) # append cost of parent set


