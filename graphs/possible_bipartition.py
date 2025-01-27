# Can be used for BFS
from collections import  deque
# from curses import COLORS 

COLORS = ["blue", "green"]

def dfs(dislikes, current_node, painted_graph, current_color):
    neighbors = dislikes[current_node]
    next_color = (current_color + 1) % len(COLORS)

    for neighbor in neighbors:
        color = painted_graph.get(neighbor)

        if not color:
            painted_graph[neighbor] = COLORS[next_color]
            if not dfs(dislikes=dislikes, current_node=neighbor, painted_graph=painted_graph, current_color=next_color):
                return False
        elif color != COLORS[next_color]:
            return False
    
    return True
    

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: o(n)
        Space Complexity: o(n)
    """
    painted_graph = {}
    current_color = 0

    for node in range(len(dislikes)):
        neighbors = dislikes[node]
        if not painted_graph.get(node):
            painted_graph[node] = COLORS[current_color]

            if not dfs(dislikes=dislikes, current_node=node, painted_graph=painted_graph, current_color=current_color):
                return False
    return True


    # struggled with an small syntax error and then looked at leetcode answers and solution and noticed i had set it up backwards. 