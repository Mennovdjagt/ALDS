import random
import copy
import math

class edge:

    def __init__(self, var1, var2, nactionsx, nactionsy):
        """
        Constructor for the edge class
        :param var1: the (index of the) first decision variable
        :param var2: the (index of the) second decision variable
        :param nactionsx: the number of possible values for var1
        :param nactionsy: the number of possible values for var1
        """
        self.rewards = [] #table with the local rewards
        self.x = var1
        self.y = var2
        for i in range(nactionsx):
            rew = []
            for j in range(nactionsy):
                rew.append( random.random() )
            self.rewards.append(rew)

    def localReward(self, xval, yval):
        """
        Return the local reward for this edge given the values of the connected decision variables
        :param xval: value of the first decision variable
        :param yval: value of the second decision variable
        :return: the local reward
        """
        return self.rewards[xval][yval]


class coordinationGraph:

    def __init__(self, noNodes, pEdge, noActions, seed=42):
        """
        Constructor for the coordination graph class. It generates a random graph based on a seed.

        :param noNodes: The number of vertices in the graph. Each vertex represents a decision variable.
        :param pEdge: the probability that an edge will be made
        :param noActions: the number of possible values (integers between 0 and noActions) for the decision variables
        :param seed: the pre-set seed for the random number generator
        """
        random.seed(seed)
        self.nodesAndConnections = dict() #for each node, a list of nodes it is connected to
        self.edges = dict() #A dictionary of tuples (of two decision variables) to an object of the edge class
        for i in range(noNodes): #First make sure that the entire graph is connected (connecting all nodes to the next one)
            if i == 0:
                self.nodesAndConnections[i] = [i + 1]
                self.nodesAndConnections[i+1] = [i]
                eddy = edge(i, i+1, noActions, noActions)
                self.edges[(i,i+1)] = eddy
            elif i <noNodes-1:
                self.nodesAndConnections[i].append(i + 1)
                self.nodesAndConnections[i + 1] = [i]
                eddy = edge(i, i + 1, noActions, noActions)
                self.edges[(i, i + 1)] = eddy
        tuplist = [(x, y) for x in range(noNodes) for y in range(x + 2, noNodes)]
        for t in tuplist: #Then, for each possible edge, randomly select which exist and which do not
            r = random.random()
            if r < pEdge:
                self.nodesAndConnections[t[0]].append(t[1])
                self.nodesAndConnections[t[1]].append(t[0])
                self.edges[t] = edge(t[0], t[1], noActions, noActions)
        #For reasons of structure, finally, let's sort the connection lists for each node
        for connections in self.nodesAndConnections.values():
            connections.sort()

    def evaluateSolution(self, solution):
        """
        Evaluate a solution from scratch; by looping over all edges.

        :param solution: a list of values for all decision variables in the coordination graph
        :return: the reward for the given solution.
        """
        result = 0
        for i in range(len(solution)):
            for j in self.nodesAndConnections[i]:
                if(j>i):
                    #print( "("+str(i)+","+str(j)+") -> "+str(self.edges[(i,j)].localReward(solution[i], solution[j])))
                    result += self.edges[(i,j)].localReward(solution[i], solution[j])
        return result

    def evaluateChange(self, oldSolution, variableIndex, newValue):
        """
        :param oldSolution: The original solution
        :param variableIndex: the index of the decision variable that is changing
        :param newValue: the new value for the decision variable
        :return: The difference in reward between the old solution and the new solution (with solution[variableIndex] set to newValue)
        """

        oldReward = self.evaluateSolution(oldSolution)      # get the reward of the old solution
        oldSolution[variableIndex] = newValue               # set the oldsolution[variableIndex] to newValue
        newReward = self.evaluateSolution(oldSolution)      # get a new reward with the changed oldSolution (using newValue at variableindex)

        delta = newReward - oldReward                       # calculate the difference in reward between the old solution and the new solution

        return delta

def localSearch4CoG(coordinationGraph, initialSolution):
    """
    :param coordinationGraph: the coordination graph to optimise for
    :param initialSolution: an initial solution for the coordination graph
    :return: a new solution (a local optimum)
    """

    solution = copy.copy(initialSolution)
    stop = False
    vars = list(coordinationGraph.nodesAndConnections.keys())                   # a list of the decisions
    random.shuffle(vars)                                                        # randomize the list

    while vars:                                                                 # loop through all var objects
        i = vars.pop(0)                                                         # put var in i and remove it out of vars
        for decision in range(3):
            delta = coordinationGraph.evaluateChange(solution, i, decision)     # get the difference in reward
            if delta > 0:
                solution[i] = decision                                          # the new solution if the value is positive
                random.shuffle(vars)                                            # rerandomize the list
                break

    return solution

def multiStartLocalSearch4CoG(coordinationGraph, noIterations):
    """
    :param coordinationGraph: the coordination graph to optimise for
    :param noIterations:  the number of times local search is run
    :return: the best local optimum found and its reward
    """
    solution = None     # the approximate solution (the local optimum)
    val = -math.inf     # not sure yet what negative infinity means (could be something like this: -math.inf)

    for i in range(0, noIterations-1):
        a = [random.randrange(3)] * len(coordinationGraph.nodesAndConnections.keys())   # a random value for each decision variable (a random state * the amount of nodes)
        a = localSearch4CoG(coordinationGraph, a)                                       # check a solution on local search
        newVal = coordinationGraph.evaluateSolution(a)                                  # get a new reward

        if newVal > val:        # check if the new reward is better than the old one
            solution = a        # change the solution to the new solution called a
            val = newVal        # make the reward the new reward

    return solution, val        # return the solution and the reward


def iteratedLocalSearch4CoG(coordinationGraph, pChange, noIterations):
    """
    :param coordinationGraph: the coordination graph to optimise for
    :param pChange: the perturbation strength, i.e., when mutating the solution, the probability for the value of a given
                    decision variable to be set to a random value.
    :param noIterations:  the number of iterations
    :return: the best local optimum found and its reward
    """
    solution = [-1]*len(coordinationGraph.nodesAndConnections.keys())   # the approximate solution (a local optimum)
    val = -math.inf                                                     # the reward (negative infinity)

    for i in range(0, noIterations-1):                          # loop through all noIterations
        a = solution                                            # create a new variable called a to store the solution
        for j in coordinationGraph.nodesAndConnections.keys():  # loop through all nodes
            r = random.uniform(0, 1)                            # get a random number between 0 and 1
            if r < pChange:                                     # check if the random(0, 1) is smaller than the number of trails
                a[j] = random.randrange(3)                      # change a by changing the value of variable j to a random value

        a = localSearch4CoG(coordinationGraph, a)               # check the value of the new solution
        newVal = coordinationGraph.evaluateSolution(a)          # get the new reward

        if newVal > val:        # check if the new reward is better than the old reward
            solution = a        # change the solution to the new solution
            val = newVal        # set the old reward to the new reward

    return solution, val        # return the solution and the reward


nVars = 50
nActs = 3
cog = coordinationGraph(nVars,1.5/nVars,nActs)
#print(cog.nodesAndConnections)
#print(cog.edges)

values = []
bestValue = 0
pChangeValue = 0

print("Local search: " + str(cog.evaluateSolution(localSearch4CoG(cog, [2]*nVars))))
print("Multi-start local search: " + str(multiStartLocalSearch4CoG(cog, 10)[1]))
print("Iterated local search: " + str(iteratedLocalSearch4CoG(cog, 0.0, 10)[1]))

for i in range(0, 1000):
    value = iteratedLocalSearch4CoG(cog, (0.001 * i), 10)[1]
    if bestValue < value:
        bestValue = value
        pChangeValue = 0.001 * i

print("Best value: " + str(bestValue))
print("Best pChange value: " + str(pChangeValue))