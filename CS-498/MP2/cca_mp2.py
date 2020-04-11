from collections import defaultdict 


class ListClass:
    def __init__(self):
        self.key = ""
        self.distance = 0
        self.source = ""
        self.destination = ""

class Graph:
    

  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list)
        #self.visited = False 


    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    #visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue

    def bfs(self,visited, graph, node, destination,uniqueList, compare):
        content = -1
        visited.append(node)
        self.queue.append(node)

        while self.queue:
            s = self.queue.pop(0) 
            if destination != "" and s == destination and node + "->" + destination not in visited:
                comp = ListClass()
                
                if node == destination:
                    #print(node + "->" + destination + "0")
                    content = 0
                    comp.distance = content
                    
                else:
                    #print(node + "->" + destination + "2")  
                    content = 2
                    comp.distance = content
                    
                if node+destination not in compare:
                        comp.key = node+destination
                        comp.source = node
                        comp.destination = destination
                        compare.append(node+destination)
                        uniqueList.append(comp)
            for neighbour in graph[s]:
                if s + "->" + neighbour not in visited:
                    #print(s + "->" + neighbour + "1")                    
                    visited.append(s + "->" + neighbour)
                    comp = ListClass()

                    if s == neighbour:
                        content = 0
                        comp.distance = content
                    else:
                         content = 1
                         comp.distance = content
                         
                    if s+neighbour not in compare:
                        comp.key = s+neighbour
                        comp.source = s
                        comp.destination = neighbour
                        compare.append(s+neighbour) 
                        uniqueList.append(comp)    

                    self.queue.append(neighbour)



#str_cities = "a1->a2,a2->a3,a3->a4,a1->a5,a1->a6,a2->a7,a3->a7,a6->a8,a9->a2,a9->a4,a10->a11,a11->a5,a7->a11,a12->a2,a9->a12"
#str_cities ="SJC->SFO,SFO->DAL,SJC->LAS,LAS->PHX,PHX->DAL"
str_cities = "New York->New Jersey,New Jersey->Boston,\
Boston->Philadelphia,New York->Washington,New York->Miami,\
New Jersey->Houston,Boston->Houston,Miami->Austin,Los Angeles->New Jersey,\
Los Angeles->Philadelphia,San Francisco->Las Vegas,Las Vegas->Washington,Houston->Las Vegas,\
Chicago->New Jersey,Los Angeles->Chicago"

city_list = str_cities.split(',')
initialSource = city_list[0].split('->')
g = Graph()
for city in range(len(city_list)):
        split_city = city_list[city].split('->')
        g.addEdge(split_city[0],split_city[1])
visited = []
uniqueList = []
compare = []
g.bfs(visited,g.graph,initialSource[0],"",uniqueList,compare)

for city in range(len(city_list)):
    split_city = city_list[city].split('->')
    for destination_city in range(1,len(city_list)):
        visited = []
        split_destination_city = city_list[destination_city].split('->')
        g.bfs(visited,g.graph,split_city[0],split_destination_city[1],uniqueList,compare)

for ls in uniqueList:
    print(ls.key, ls.distance)




