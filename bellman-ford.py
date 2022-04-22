inf = float("inf")


def bellman_ford(graph, start_index):
    """Computes the shortest path from an index to all other indexes using
    Bellman-Ford algorithm. This algorithm only returns the cost from the
    starting node to other nodes, but technically computes all shortest paths
    from all nodes to all other nodes. Tweaking the return values can return 
    other results.

    Parameters:
    graph (matrix): A graph represented in adjacency matrix form that can be
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
    graph_len = len(graph)
    past_costs = [[inf] * graph_len for i in range(graph_len)]
    for i in range(graph_len):
        past_costs[i][i] = 0
    shortest_paths = [[[i]] * graph_len for i in range(graph_len)]
    
    for i in range(graph_len - 2):
        curr_costs = past_costs.copy()
        # Updates estimated cost list by checking neighbor's cost lists
        for curr_index in range(graph_len):
            for neighbor_index in range(graph_len):
                edge_weight = graph[curr_index][neighbor_index]
                # Check if the cost to neighbor's neighbor is less than current
                for j in range(graph_len):
                    old_cost = past_costs[curr_index][j]
                    new_cost = edge_weight + past_costs[neighbor_index][j]
                    if (new_cost < old_cost):
                        # Update the cost and path
                        curr_costs[curr_index][j] = new_cost
                        new_path = [curr_index]
                        new_path.extend(shortest_paths[neighbor_index][j])
                        shortest_paths[curr_index][j] = new_path
        past_costs = curr_costs
    
    return past_costs[start_index], shortest_paths[start_index]


def bellman_ford_test():
    inf = float("inf")
    print("--- Test 1 ---")
    matrix = [[inf,   3,   1,   5, inf],
              [  3, inf, inf,   1, inf],
              [  1, inf, inf, inf,   9],
              [  5,   1, inf, inf,   2],
              [inf, inf,   9,   2, inf]]
    costs, paths = bellman_ford(matrix, 0)
    print(costs) # [0, 3, 1, 4, 6]
    print(paths) # [[0], [0, 1], [0, 2], [0, 1, 3], [0, 1, 3, 4]]

    print("--- Test 2 ---")
    matrix = [[inf,   4,   1, inf],
              [inf, inf,   1,   2],
              [inf,   1, inf, inf],
              [inf, inf, inf, inf]]
    costs, paths = bellman_ford(matrix, 0)
    print(costs) # [0, 2, 1, 4]
    print(paths) # [[0], [0, 2, 1], [0, 2], [0, 2, 1, 3]]


if (__name__ == "__main__"):
    bellman_ford_test()