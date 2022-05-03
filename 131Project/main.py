from flask import Flask, redirect, url_for, render_template
from dijkstra import dijkstra_test
from test import test
import string
import fibheap
import time
from graphGenerate import Graph


inf = float("inf")
#redirct and url_for allows redirect from a specific function
#grab an html file and render it as ome page

app = Flask(__name__) #create instance of flask web app

#define how to access the certain page

#@app.route("/") #default will go to home page. can define certain
                #pages after '/'

'''
@app.route("/", methods=['GET','POST'])
def index():
    return "AlgoFlights"
'''

def dijkstra(g: Graph, start_name: string):
    """Computes the shortest path from an index to all other indexes using
    dijkstra's algorithm.
    Parameters:
    graph (matrix): A graph represented in adjacency list form that can be
        directed or undirected and must not contain any negative edges.
    start_index (int): The index of the starting node in the graph.
    Return:
    shortest_estimate (list): The estimated costs from the starting node to 
        all other nodes in list form.
    shortest_paths (list of lists): The shortest paths from the starting node
        to all other nodes. Each path is formatted as a list with the nodes 
        that must be traversed to get to the end node, including the starting
        node.
    """
    graph_len = len(g.graph)
    unsure_nodes = {}
    find_nodes = {}
    dist = fibheap.Fheap()
    shortest_estimate = [None] * graph_len
    shortest_paths = [[start_name]] * graph_len

    # Build fibonacci heap to store distances and unsure node list
    for i in range(graph_len):
        if (g.labelList[i] == start_name):
            newNode = fibheap.Node(0)
        else:
            newNode = fibheap.Node(inf)
        dist.insert(newNode)
        unsure_nodes[f"{newNode}"] = i
        find_nodes[f"{i}"] = newNode

    # While unsure nodes exist, get the minimum of them and update estimated costs
    while (unsure_nodes):
        curr_node = dist.extract_min()
        curr_index = unsure_nodes[f"{curr_node}"]
        curr_cost = curr_node.key
        curr_path = shortest_paths[curr_index]
        num_neighbors = len(g.graph[curr_index])

        # Calculate the new cost to the neighbor and compare it against old cost
        for i in range(num_neighbors):
            for j in range(len(g.labelList)):
                if (g.graph[curr_index][i][0] == g.labelList[j]):
                    neighbor_index = j
                    break
            neighbor_node = find_nodes[f"{neighbor_index}"]
            curr_neighbor_cost = neighbor_node.key
            new_neighbor_cost = curr_cost + g.graph[curr_index][i][1]
            if (new_neighbor_cost < curr_neighbor_cost):
                # Update the cost and path
                dist.decrease_key(neighbor_node, new_neighbor_cost)
                new_path = curr_path.copy()
                new_path.append(g.labelList[neighbor_index])
                shortest_paths[neighbor_index] = new_path
        
        # Mark current node as sure and save its cost
        unsure_nodes.pop(f"{curr_node}")
        shortest_estimate[curr_index] = curr_cost
    
    return shortest_estimate, shortest_paths


def dijkstra_test():
    print("--- Test 3 ---")
    textPath="airports.txt"
    cityList = Graph.citiesGen(textPath)
    adjGraph=Graph(len(cityList))
    adjGraph.populate(cityList)
    costs, paths = dijkstra(adjGraph, 'SJC')
    print(costs)
    print(paths)
    return costs,paths






@app.route("/d")
def dynamic_page():
    return dijkstra_test()

@app.route("/", methods = ['GET','POST'])
def home(): #returns what is being displayed on the page using html file
    return render_template("home.html") #inline 
@app.route("/test", methods = ['GET','POST'])
def test():
    start_time = time.time() #start time of the dijkstra's alogrithm
    value,value1 = dijkstra_test()
    timeElapsed = time.time() - start_time #end time of dijkstra's algorithm
    return render_template("test.html", value = value, value1 = value1, timeElapsed = timeElapsed) #passes the value to html file

if __name__ == "main": #runs the app
    app.run(port=5000, debug = True) #allows for changes to be seen without restarting the server
