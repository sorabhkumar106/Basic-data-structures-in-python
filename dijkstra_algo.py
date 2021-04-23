import sys
import  heapq
class Edge(object):
    def __init__(self,weight,startVertex,targetVertex):
        self.weight=weight
        self.startVertex=startVertex
        self.targetVetex=targetVertex

class Node(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjencyList=[]
        self.minDistance=sys.maxsize
    def __cmp__(self, otherVertex):
        return self.__cmp__(self.minDistance,otherVertex.minDistance)
    def __lt__(self, other):
        selfPriortty=self.minDistance
        otherProrty=other.minDistance
        return selfPriortty<otherProrty

class Algorithem(object):
    def calculateShortestPath(self,vertexList,startVertex):
        q=[]
        startVertex.minDistance=0
        heapq.heappush(q,startVertex)
        while len(q)>0:
            actualVertex=heapq.heappop(q)
            for edge in actualVertex.adjencyList:
                u=edge.startVertex
                v=edge.targetVetex