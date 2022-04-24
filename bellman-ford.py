from graphGenerate import Graph
import string


inf = float("inf")


def bellman_ford(g: Graph, start_name: string):
    """Computes the shortest path from an index to all other indexes using
    Bellman-Ford algorithm. This algorithm only returns the cost from the
    starting node to other nodes, but technically computes all shortest paths
    from all nodes to all other nodes. Tweaking the return values can return 
    other results.

    Parameters:
    graph (matrix): A graph represented in adjacency list form that can be
        directed or undirected and must not contain any negative cycles.
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
    past_costs = [[inf] * graph_len for i in range(graph_len)]
    for i in range(graph_len):
        past_costs[i][i] = 0
    shortest_paths = [[[f'{g.labelList[i]}']] * graph_len for i in range(graph_len)]
    
    for k in range(graph_len - 2):
        curr_costs = past_costs.copy()
        # Updates estimated cost list by checking neighbor's cost lists
        for curr_index in range(graph_len):
            num_neighbors = len(g.graph[curr_index])
            for i in range(num_neighbors):
                for j in range(len(g.labelList)):
                    if (g.graph[curr_index][i][0] == g.labelList[j]):
                        neighbor_index = j
                        break
                edge_weight = g.graph[curr_index][i][1]
                # Check if the cost to neighbor's neighbor is less than current
                for j in range(graph_len):
                    old_cost = past_costs[curr_index][j]
                    new_cost = edge_weight + past_costs[neighbor_index][j]
                    if (new_cost < old_cost):
                        # Update the cost and path
                        curr_costs[curr_index][j] = new_cost
                        new_path = [g.labelList[curr_index]]
                        new_path.extend(shortest_paths[neighbor_index][j])
                        shortest_paths[curr_index][j] = new_path
        past_costs = curr_costs
    
    for i in range(len(g.labelList)):
        if (start_name == g.labelList[i]):
            start_index = i
            break
    return past_costs[start_index], shortest_paths[start_index]


def bellman_ford_test():
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
    costs, paths = bellman_ford(g, '0')
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
    costs, paths = bellman_ford(g, '0')
    print(costs) # [0, 2, 1, 4]
    print(paths) # [['0'], ['0', '2', '1'], ['0', '2'], ['0', '2', '1', '3']]

    print("--- Test 3 ---")
    textPath="airports.txt"
    cityList = Graph.citiesGen(textPath)
    adjGraph=Graph(len(cityList))
    adjGraph.populate(cityList)
    costs, paths = bellman_ford(adjGraph, 'SJC')
    print(costs)
    print(paths)

if (__name__ == "__main__"):
    bellman_ford_test()