class Node:
    def __init__(self):
        self.N                      #the number of visits to the node
        self.Q                      #the number of wins plus 0.5 times the number of draws
        self.parent = None          # the parent above
        self.children = {}          # all the children

    def FindSpotToExpand(self, node):
        if node.is_terminal():
            print("the end")
        if node not in self.children:
            #create new node to expand
            #add node to node's children
            return node.find_random_child()
        #get node with highest uct value
        return FindSpotToExpand(node)

    def Rollout(self, node):
        while  is not terminal:
            #a = random action/move in state s
            #s = the new game state after executing a
        return s