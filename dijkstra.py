import string
import fibheap
from graphGenerate import Graph


inf = float("inf")


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
    print("--- Test 1 ---")
    g = Graph(5)
    matrix = [[inf,   3,   1,   5, inf],
              [  3, inf, inf,   1, inf],
              [  1, inf, inf, inf,   9],
              [  5,   1, inf, inf,   2],
              [inf, inf,   9,   2, inf]]
    for i in range(len(matrix)):
        g.labelList[i] = f'{i}'
        for j in range(len(matrix[i])):
            if (matrix[i][j] == inf):
                continue
            g.graph[i].append([f'{j}', matrix[i][j]])
    costs, paths = dijkstra(g, '0')
    print(costs) # [0, 3, 1, 4, 6]
    print(paths) # [['0'], ['0', '1'], ['0', '2'], ['0', '1', '3'], ['0', '1', '3', '4']]

    print("--- Test 2 ---")
    g = Graph(4)
    matrix = [[inf,   4,   1, inf],
              [inf, inf,   1,   2],
              [inf,   1, inf, inf],
              [inf, inf, inf, inf]]
    for i in range(len(matrix)):
        g.labelList[i] = f'{i}'
        for j in range(len(matrix[i])):
            if (matrix[i][j] == inf):
                continue
            g.graph[i].append([f'{j}', matrix[i][j]])
    costs, paths = dijkstra(g, '0')
    print(costs) # [0, 2, 1, 4]
    print(paths) # [['0'], ['0', '2', '1'], ['0', '2'], ['0', '2', '1', '3']]

    print("--- Test 3 ---")
    textPath="airports.txt"
    cityList = Graph.citiesGen(textPath)
    adjGraph=Graph(len(cityList))
    adjGraph.populate(cityList)
    costs, paths = dijkstra(adjGraph, 'SJC')
    print(costs)
    print(paths)

if (__name__ == "__main__"):
    dijkstra_test()