import fibheap


inf = float("inf")


def dijkstra(graph, start_index):
    """Computes the shortest path from an index to all other indexes using
    dijkstra's algorithm.

    Parameters:
    graph (matrix): A graph represented in adjacency matrix form that can be
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
    graph_len = len(graph)
    unsure_nodes = {}
    find_nodes = {}
    dist = fibheap.Fheap()
    shortest_estimate = [None] * graph_len
    shortest_paths = [[start_index]] * graph_len

    # Build fibonacci heap to store distances and unsure node list
    for i in range(graph_len):
        if (i == start_index):
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

        # Calculate the new cost to the neighbor and compare it against old cost
        for neighbor_index in range(graph_len):
            if (neighbor_index == curr_index):
                continue
            neighbor_node = find_nodes[f"{neighbor_index}"]
            curr_neighbor_cost = neighbor_node.key
            new_neighbor_cost = curr_cost + graph[curr_index][neighbor_index]
            if (new_neighbor_cost < curr_neighbor_cost):
                # Update the cost and path
                dist.decrease_key(neighbor_node, new_neighbor_cost)
                new_path = curr_path.copy()
                new_path.append(neighbor_index)
                shortest_paths[neighbor_index] = new_path
        
        # Mark current node as sure and save its cost
        unsure_nodes.pop(f"{curr_node}")
        shortest_estimate[curr_index] = curr_cost
    
    return shortest_estimate, shortest_paths


def dijkstra_test():
    print("--- Test 1 ---")
    matrix = [[inf,   3,   1,   5, inf],
              [  3, inf, inf,   1, inf],
              [  1, inf, inf, inf,   9],
              [  5,   1, inf, inf,   2],
              [inf, inf,   9,   2, inf]]
    costs, paths = dijkstra(matrix, 0)
    print(costs) # [0, 3, 1, 4, 6]
    print(paths) # [[0], [0, 1], [0, 2], [0, 1, 3], [0, 1, 3, 4]]

    print("--- Test 2 ---")
    matrix = [[inf,   4,   1, inf],
              [inf, inf,   1,   2],
              [inf,   1, inf, inf],
              [inf, inf, inf, inf]]
    costs, paths = dijkstra(matrix, 0)
    print(costs) # [0, 2, 1, 4]
    print(paths) # [[0], [0, 2, 1], [0, 2], [0, 2, 1, 3]]


if (__name__ == "__main__"):
    dijkstra_test()