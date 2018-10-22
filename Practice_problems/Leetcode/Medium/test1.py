"""
Evaluate Division
Difficulty:Medium

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
#######################################
'''
Ideas:
Need to find values for all the input variables. Can use substitution to get values of one variable in terms of another.
eg. a/b = 2.0 b/c = 3.0
b = 2/a
a = 2b
c = 3b

a/c = 2b / 3b
b / a = b / 2b

Use a dictionary where the key is the variable, and the value is a list of the different ways to represent the variable
When given a query perform bfs to build a dictionary of the numerator and denominator to find different ways of representing the numerator
and denominator. Iteratate through the numerator dictionary to see if the same variable appears in the denominator dictionary. If it does then append
the numerator value / denominator value

Performing BFS takes O(N) time, where N is the total number of nodes in the graph, which is 2*number of equations, since each equation will contribute
at most 2 nodes to the graph
Total time complexity is O(M*N), where M is the number of queries
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        variable_repr = {}

        for i in range(len(equations)):
            numerator, denominator = equations[i]
            cur_val = values[i]

            if numerator in variable_repr:
                variable_repr[numerator].append([cur_val, denominator])
            else:
                variable_repr[numerator] = [[cur_val, denominator]]
            
            if denominator in variable_repr:
                variable_repr[denominator].append([1/cur_val, numerator])
            else:
                variable_repr[denominator] = [[1/cur_val, numerator]]
        
        answers = []
        for query in queries:
            numerator, denominator = query
            # Stores representations for the num and denom vals. key is the new variable, and value is the coefficient.
            num_val_repr = {}
            denom_val_repr = {}
            if numerator in variable_repr and denominator in variable_repr:
                num_val_repr = self.find_representations(numerator, variable_repr)
                denom_val_repr = self.find_representations(denominator, variable_repr)
                for key in num_val_repr:
                    if key in denom_val_repr:
                        answers.append(num_val_repr[key] / denom_val_repr[key])
                        break
            else:
                answers.append(-1.0)
        
        return answers
    
    # Performs BFS on variable_repr to find different representations of variable
    # and returns a dictionary with the key as the new variable, and value as the coefficent
    # that is used to convert variable to new variable
    def find_representations(self, variable, variable_repr):
        var_val_repr = {}
        seen = set()
        queue = []
        for ele in variable_repr[variable]:
            queue.append([ele, 1])
        
        while len(queue) != 0:
            cur_node, cur_coeff = queue.pop(0)
            if cur_node[1] not in seen:
                seen.add(cur_node[1])

                # Adds a new variable and its coefficient to the dictionary
                # Must multiply for cur_coeff, to make the transition from the original variable to the new variable
                var_val_repr[cur_node[1]] = cur_node[0] * cur_coeff
                cur_coeff = cur_node[0] * cur_coeff
                for ele in variable_repr[cur_node[1]]:
                    queue.append([ele, cur_coeff])
        
        return var_val_repr
        