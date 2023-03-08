import gridworld


def find_path(neighbour_fn,
			  start,
			  goal,
			  visited,
			  reachable = lambda pos: True,
			  depth = 100000):
	
	#The reachable function returns true if the given node is not blocked by a wall.


	"""
	#TODO: 
	Returns the path between two nodes as a list of nodes using depth first search.
	If no path can be found, an empty list is returned.

	neighbour_fn is a successor function and returns the set of all the neighbouring nodes.
	start is the start node
	goal : is the goal node
	visited is the set of nodes which are already visited, explored
	The reachable function takes a tile as an argument and returns false if there is a wall on top of the tile or if the tile is outside of the grid map.
	depth is the depth that your function should avoid searching at any deeper depth.
	
	"""
	stack = [(start, [start])]
    
    # Loop while the stack is not empty
	while stack:
        # Pop the top node from the stack and check if it is the goal node
		node, path = stack.pop()
		if node == goal:
			return path
        
        # Mark the node as visited and get its neighbours
		visited.append(node)
		neighbours = neighbour_fn(node)
        
        # Loop over the neighbours
		for neighbour in neighbours:
            # Check if the neighbour is reachable and has not been visited yet
			if reachable(neighbour) and neighbour not in visited:
                # Check if the depth limit has been reached
				if len(path) < depth:
                    # Add the neighbour to the stack along with its path from start
					stack.append((neighbour, path + [neighbour]))
    
    # If the function reaches the end of the loop without finding the goal node, return an empty list
	return []
