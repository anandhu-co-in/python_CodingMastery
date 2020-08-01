from distutils.command.install import install


class Graph:
    def __init__(self):
        self.adjacencyList = {}
        print("Created Adj List ={}".format(self.adjacencyList))

    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []

    def addEdge(self, v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)

    def removeEdge(self, vertex1, vertex2):
        print(self.adjacencyList)
        print("Removing Edge {}--{}".format(vertex1, vertex2))

        self.adjacencyList[vertex1] = list(set(self.adjacencyList[vertex1]) - set([vertex2]))
        self.adjacencyList[vertex2] = list(set(self.adjacencyList[vertex2]) - set([vertex1]))

    def removeVertex(self, vertex):
        # When a vertex is removed, we need to remove all edges from others into it

        while len(self.adjacencyList[vertex]) != 0:
            removeVertex = self.adjacencyList[vertex].pop()
            print(removeVertex)
            self.removeEdge(vertex, removeVertex)
        del self.adjacencyList[vertex]


    def DFSRecursive(self,startVertex):

        result=[]
        visited={}

        def recFun(currentVertex):
            visited[currentVertex]=True
            result.append(currentVertex)
            for x in self.adjacencyList[currentVertex]:
                if x not in visited:
                    recFun(x)
        recFun(startVertex)

        print(result)


    def DFSIterative(self,startVertex):

        queue=[startVertex]
        result=[]
        visited={startVertex:True}  #This will contains items we have stacked!

        while len(queue)!=0:
            current=queue.pop()
            result.append(current)
            for x in self.adjacencyList[current]:
                if x not in visited :
                    queue.append(x)
                    visited[x]=True
        print(result)



    def BFS(self,startVertex):

        stack=[startVertex]
        result=[]
        visited={startVertex:True}  #This will contains items we have stacked!

        while len(stack)!=0:
            current=stack.pop(0)
            result.append(current)
            for x in self.adjacencyList[current]:
                if x not in visited :
                    stack.append(x)
                    visited[x]=True
        print(result)










myGraph = Graph()

myGraph.addVertex("A")
myGraph.addVertex("B")
myGraph.addVertex("C")
myGraph.addVertex("D")
myGraph.addVertex("E")
myGraph.addVertex("F")


myGraph.addEdge("A", "B")
myGraph.addEdge("A", "C")
myGraph.addEdge("B","D")
myGraph.addEdge("C","E")
myGraph.addEdge("D","E")
myGraph.addEdge("D","F")
myGraph.addEdge("E","F")

print(myGraph.adjacencyList)

myGraph.DFSRecursive("A")
myGraph.DFSIterative("A")
myGraph.BFS("A")
