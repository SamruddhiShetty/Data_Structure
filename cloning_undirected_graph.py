class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #this is solved using dfs 
        if node==None:
            return None
        #in this map we store the cloned graph 
        visited={}
        def create_clone(prev, current):
            nonlocal visited
            if current not in visited:
                visited[current]=Node(current.val)
                #this is the place where we iterate through the original graph
                for each in current.neighbors:
                    #we cannot reach the neighbors without using the list of neighbor nodes in every node
                    create_clone(current, each)
            
            if prev:
                #assigning the nodes in the dictionary with its neighbors
                visited[prev].neighbors.append(visited[current])
        create_clone(None, node)
        return visited[node]
