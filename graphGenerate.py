from math import radians, cos, sin, asin, sqrt

planeRange=3148 #range of CRJ200 in kilometers

class Graph:
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[]
        self.labelList=[]
        for i in range(self.V): #fill each list with empty spots that we can fill with data
            self.graph.append([])
            self.labelList.append([])
    
    def populate(self, cityList): #adding nodes if the distance is shorter than our plane range
        for i in range(self.V):
            self.labelList[i]=cityList[i][0]
            for j in range(self.V):
                d=Graph.distance(cityList[i][1], cityList[j][2], cityList[j][1], cityList[i][2])
                if(d<planeRange and d!=0):
                    self.graph[i].append([cityList[j][0],d])

    def printlist(self): #outputs the entire adjacency list beginning with the source followed by destinations
        for i in range(self.V):
            print(f"Starting airport: {self.labelList[i]}")
            for obj in self.graph[i]:
                print(f"Airport: {obj[0]}, Distance: {obj[1]}")

    def printNode(self, index): #output a single list based on index
        print(f"Starting airport: {self.labelList[index]}")
        for obj in self.graph[index]:
            print(f"Airport: {obj[0]}, Distance: {obj[1]}")

    def distance(latitudeA, longitudeA, latitudeB, longitudeB):
        radius = 6371 #radius of earth in kilometers
        latitudeA = radians(latitudeA)
        latitudeB = radians(latitudeB)
        longitudeA = radians(longitudeA)
        longitudeB = radians(longitudeB)
        deltaLat = abs(latitudeA - latitudeB)
        delatLon = abs(longitudeA - longitudeB)
        x = sin(deltaLat / 2)**2 + cos(latitudeA) * cos(latitudeB) * sin(delatLon / 2)**2
        y = 2 * asin(sqrt(x))
        return (y * radius) #distance between two points in kilometers

    def citiesGen(filePath):
        buffer=[] #temp storage for txt strings
        cities=[] #list of lists containing airport label, latitude, and longitude
        f=open(filePath,"r")
        buffer.extend(f.readlines())
        for i in range(len(buffer)): #Taking the strings read from txt file and converting to list of lists
          buffer[i]=buffer[i].replace("\n","")
          cities.append(buffer[i].split())
          cities[i][1]=float(cities[i][1])
          cities[i][2]=float(cities[i][2])
        f.close()
        return cities

def main():
    textPath="airports.txt"
    cityList = Graph.citiesGen(textPath)
    print(cityList)

    adjGraph=Graph(len(cityList))

    adjGraph.populate(cityList)
    print(adjGraph.graph[0])
    print(adjGraph.graph[1])
    adjGraph.printlist()

    for i in range(adjGraph.V):
        adjGraph.printNode(i)

if (__name__ == "__main__"):
    main()