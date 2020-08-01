import math


class node:
    def __init__(self, v, p):
        self.value = v
        self.priority = p

class PriorityQueue:

    def __init__(self):
        self.values = []

    def enqueue(self, val, prio):
        newNode = node(val, prio)
        self.values.append(newNode)
        self.bubbleUp()

    def bubbleUp(self):
        i = len(self.values) - 1
        current = self.values[i]
        while (i > 0):
            parentI = math.floor((i - 1) / 2)
            parent = self.values[parentI]
            if parent.priority <= current.priority: break
            self.values[parentI] = current
            self.values[i] = parent
            i = parentI

    def dequeue(self):

        if len(self.values) == 0:
            print("Heap Empty. No max value present")
            return None
        else:
            value = self.values[0].value
            lastval = self.values.pop()
            if len(self.values) > 0:
                self.values[0] = lastval
                self.syncDown()
            return value

    def syncDown(self):

        parentId = 0
        length = len(self.values)

        while (True):

            child1Id = 2 * parentId + 1
            child2Id = 2 * parentId + 2

            swap = None

            if (child1Id < length and self.values[child1Id].priority <= self.values[parentId].priority):
                swap = child1Id

            if (swap != None and child2Id < length and self.values[child2Id].priority <= self.values[
                swap].priority) or (
                    swap == None and child2Id < length and self.values[child2Id].priority <= self.values[
                parentId].priority):
                swap = child2Id

            if swap != None:
                self.values[swap], self.values[parentId] = self.values[parentId], self.values[swap]
                parentId = swap

            else:
                break


class weightedGraph:
    def __init__(self):
        self.adjacencyList = {}
        print("Created Adj List ={}".format(self.adjacencyList))

    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []

    def addEdge(self, v1, v2, weight):
        self.adjacencyList[v1].append([v2, weight])
        self.adjacencyList[v2].append([v1, weight])

    def dijskstras(self, start, end):

        previous = {}
        distances = {}
        result = []
        prioNodes = PriorityQueue()

        for x in self.adjacencyList:
            if x == start:
                distances[x] = 0
                prioNodes.enqueue(x, 0)
            else:
                distances[x] = math.inf
                prioNodes.enqueue(x, math.inf)
            previous[x] = None

        while (len(prioNodes.values) != 0):

            smallest = prioNodes.dequeue()

            if (smallest == end):
                print("COMPLETED")
                print("Previous ----> {}".format(previous))
                print("Distances ---> {}".format(distances))
                while (smallest != None):
                    result.append(smallest)
                    smallest = previous[smallest]

                result.reverse()
                print("Shortest path from {} to {} is {}".format(start,end,result))
                break
            else:
                for neighbour in self.adjacencyList[smallest]:

                    currentDistance = distances[smallest] + neighbour[1]

                    if currentDistance < distances[neighbour[0]]:
                        distances[neighbour[0]] = currentDistance
                        previous[neighbour[0]] = smallest
                        prioNodes.enqueue(neighbour[0], currentDistance)
                        print("New Small distance to {} via {} is {}".format(neighbour[0], smallest, currentDistance))


graph = weightedGraph()

graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");

graph.addEdge("A", "B", 4);
graph.addEdge("A", "C", 2);
graph.addEdge("B", "E", 3);
graph.addEdge("C", "D", 2);
graph.addEdge("C", "F", 4);
graph.addEdge("D", "E", 3);
graph.addEdge("D", "F", 1);
graph.addEdge("E", "F", 1);

print(graph.adjacencyList)

graph.dijskstras("A", "E")


# Output
# Shortest path from A to E is ['A', 'C', 'D', 'F', 'E']


















# class PriorityQueue {
#   constructor(){
#     this.values = [];
#   }
#   enqueue(val, priority) {
#     this.values.push({val, priority});
#     this.sort();
#   };
#   dequeue() {
#     return this.values.shift();
#   };
#   sort() {
#     this.values.sort((a, b) => a.priority - b.priority);
#   };
# }


# class WeightedGraph {
#     constructor() {
#         this.adjacencyList = {};
#     }
#
#     addVertex(vertex){
#         if(!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
#     }
#     addEdge(vertex1,vertex2, weight){
#         this.adjacencyList[vertex1].push({node:vertex2,weight});
#         this.adjacencyList[vertex2].push({node:vertex1, weight});
#     }


#     Dijkstra(start, finish){
#         const nodes = new PriorityQueue();
#         const distances = {};
#         const previous = {};
#         let path = [] //to return at end
#         let smallest;
#         //build up initial state
#         for(let vertex in this.adjacencyList){
#             if(vertex === start){
#                 distances[vertex] = 0;
#                 nodes.enqueue(vertex, 0);
#             } else {
#                 distances[vertex] = Infinity;
#                 nodes.enqueue(vertex, Infinity);
#             }
#             previous[vertex] = null;
#         }

#         // as long as there is something to visit
#         while(nodes.values.length){
#             smallest = nodes.dequeue().val;
#             if(smallest === finish){
#                 //WE ARE DONE
#                 //BUILD UP PATH TO RETURN AT END
#                 while(previous[smallest]){
#                     path.push(smallest);
#                     smallest = previous[smallest];
#                 }
#                 break;
#             }


#             if(smallest || distances[smallest] !== Infinity){
#                 for(let neighbor in this.adjacencyList[smallest]){
#                     //find neighboring node
#                     let nextNode = this.adjacencyList[smallest][neighbor];
#                     //calculate new distance to neighboring node
#                     let candidate = distances[smallest] + nextNode.weight;
#                     let nextNeighbor = nextNode.node;
#                     if(candidate < distances[nextNeighbor]){
#                         //updating new smallest distance to neighbor
#                         distances[nextNeighbor] = candidate;
#                         //updating previous - How we got to neighbor
#                         previous[nextNeighbor] = smallest;
#                         //enqueue in priority queue with new priority
#                         nodes.enqueue(nextNeighbor, candidate);
#                     }
#                 }
#             }
#         }
#         return path.concat(smallest).reverse();
#     }
# }
#
#
#
#
#
# var graph = new WeightedGraph()
# graph.addVertex("A");
# graph.addVertex("B");
# graph.addVertex("C");
# graph.addVertex("D");
# graph.addVertex("E");
# graph.addVertex("F");
#
# graph.addEdge("A","B", 4);
# graph.addEdge("A","C", 2);
# graph.addEdge("B","E", 3);
# graph.addEdge("C","D", 2);
# graph.addEdge("C","F", 4);
# graph.addEdge("D","E", 3);
# graph.addEdge("D","F", 1);
# graph.addEdge("E","F", 1);
# graph.Dijkstra("A", "E");
#
#
# #
# # // ["A", "C", "D", "F", "E"]
