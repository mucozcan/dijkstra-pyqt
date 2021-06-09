

class Dijkstra():
    """Dijkstra algorithm.
    """
    def __init__(self,graph):
        """Constructor of Dijkstra object.

        Args:
            graph (dict): example graph format: #{'0': {'1': {'weight': 2}, 
                                                # '0': {'weight': 4}}, 
                                                # '1': {'0': {'weight': 2}, 
                                                # '2': {'weight': 4}}, 
                                                # '2': {'weight': 3}}, 
                                                # '2': {'1': {'weight': 3}, 
                                                # '3': {'weight': 5}, 
                                                # '3': {'2': {'weight': 5}}}
        """
        self.graph = graph
    
    def find_route(self ,start, end):
        """

        Args:
            start (string): Start node of graph.
            end (string): Target node of graph.

        Returns:
            visited (list): List of all visited nodes from start to end.
            parents (list): List of  all nodes from start to end with matched previous nodes. Kinda hard to explain :(
        """
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        unvisited = {}
        for node in self.graph:
            unvisited[node] = 0 if node==start else float("inf") # assigning start node to 0, others to infinity or any large number.

        while unvisited: # is not empty
            current_node = min(unvisited, key=unvisited.get)

            for neighbour, weight in self.graph[current_node].items():
                if neighbour in visited: # we don't wanna go backward on graph, so ignoring the neigbour if we pass through that node
                    continue
                
                if unvisited[current_node] + weight["weight"] < unvisited[neighbour]:
                    unvisited[neighbour] = unvisited[current_node] + weight["weight"]
                    parents[neighbour] = current_node
                
            visited[current_node] = unvisited[current_node]
            unvisited.pop(current_node)

            if current_node == end:
                break
        return  parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        """Formatting the shortest path between start and end.

        Args:
            parents (list): List of parents from find_route() function.
            start (string): Start node.
            end (string): End node.

        Returns:
            path (list): Shortest path.
        """

        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path
