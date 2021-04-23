import sys
class Node(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjencyList=[]
        self.minDistance=sys.maxsize

class Edge(object):
    def __init__(self,weight,startVertax,targerVertax):
        self.weight=weight
        self.startVertex=startVertax
        self.targetVertex=targerVertax

class Bellmanford(object):
    HAS_CYCLE=False
    def calculateShortestPath(self,vertaxList,edgeList,startVertax):
        startVertax.minDistance=0
        for i in range(len(vertaxList)-1):
            for edge in edgeList:
                u=edge.startVertex
                v=edge.targetVertex
                newDistance=u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance=newDistance
                    v.predecessor=u
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected.......")
                Bellmanford.HAS_CYCLE=True
                return
    def hasCycle(self,edge):
        if (edge.startVertex.minDistance+edge.weight)<edge.targetVertex.minDistance:
            return  True
        else:
            return False
    def getShortestPath(self,targetVertex):
        if not Bellmanford.HAS_CYCLE:
            print("Shortest path has found with value :",targetVertex.minDistance)
            node=targetVertex
            while node is not None:
                print(node.name)
                node=node.predecessor
        else:
            print("Negative cycle has detected......")

node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node6=Node("F")
node7=Node("G")
node8=Node("H")

edge1=Edge(5,node1,node2)
edge2=Edge(8,node1,node8)
edge3=Edge(9,node1,node5)
edge4=Edge(15,node2,node4)
edge5=Edge(12,node2,node3)
edge6=Edge(4,node2,node8)
edge7=Edge(5,node5,node8)
edge8=Edge(4,node5,node6)
edge9=Edge(20,node5,node7)
edge10=Edge(7,node8,node3)
edge11=Edge(6,node8,node6)
edge12=Edge(3,node3,node4)
edge13=Edge(11,node3,node7)
edge14=Edge(1,node6,node3)
edge15=Edge(13,node6,node7)
edge16=Edge(9,node4,node7)

edge17=Edge(1,node1,node2)
edge18=Edge(1,node2,node3)
edge19=Edge(-3,node3,node1)
node1.adjencyList.append(edge17)
node1.adjencyList.append(edge1)
node1.adjencyList.append(edge2)
node1.adjencyList.append(edge3)
node2.adjencyList.append(edge4)
node2.adjencyList.append(edge18)
node2.adjencyList.append(edge5)
node2.adjencyList.append(edge6)
node5.adjencyList.append(edge7)
node5.adjencyList.append(edge8)
node5.adjencyList.append(edge9)
node8.adjencyList.append(edge10)
node8.adjencyList.append(edge11)
node3.adjencyList.append(edge12)
node3.adjencyList.append(edge13)
node1.adjencyList.append(edge19)
node6.adjencyList.append(edge14)
node6.adjencyList.append(edge15)
node4.adjencyList.append(edge16)
vertexList=(node1,node2,node3,node4,node5,node6,node7,node8)
#edgeList=(edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16)
edgeList=(edge17,edge18,edge19)
algo=Bellmanford()
algo.calculateShortestPath(vertexList,edgeList,node1)
algo.getShortestPath(node7)
