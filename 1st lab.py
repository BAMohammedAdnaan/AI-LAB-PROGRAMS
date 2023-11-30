class Node:
    def __int__(self,v,weight):
        self.v=v
        self.weight=weight

class pathNode:
    def __int__(self,node,parent):
        self.node=node
        self.parent=parent

def addEdge(u,v,weight) :
    addEdge(u).append(Node(v,weight))
adj=[]

def GBFS(h,v,src,dest):
    openlist=[]
    closelist=[]
    openlist.append(pathNode(src,None))
    while(openlist):
        currentNode=openlist[0]
        currentIndex=0
        for i in range(len(openlist)):
            if(h[openlist[i].node] < h[currentNode.node]):
                currentNode=openlist[i]
                currentIndex=i

