# function to represent the regression tree for calculating utility of edges 

import numpy as np 

'''
- if there is no wildlife theme: 
    - if there is no animal theme, the utility is 0.1 
    - if there is a animal theme, the utility is 0.3 
- if there is a wildlife theme, we will check
    - if there is not a animals theme, the utility is 0.4
    - if there is a animals theme, the utility is 0.6 (complement effect: wildlife and animal > wildlife only + animal only)

- utility += 0.1*landmark + 0.1*environment (additive)

- if there is both landmark and garden, utility -= 0.1 (substitution effect: landmark and garden < landmark only + garden only)

For this regression tree, we will use the following rules:
params: 
- edges_vector: the feature vector for an edge. This is a numpy array of size 1 x n 
where n is the number of themes in the dataset. 
'''
def calc_edge_utility(edges_vector):
  # regression tree for calculating utility of an edge 
   utility = 0.1  # Starting with a base utility

    # Applying regression tree rules based on theme presence
    if edge_vector[64] == 0:
        if edge_vector[24] == 0:
            utility = 0.1
        else:
            utility = 0.3
    else:
        if edge_vector[24] == 0:
            utility = 0.4
        else:
            utility = 0.6

    # Second rule: landmark and environment (additive)
    utility += 0.1*edges_vector[7] + 0.1*edges_vector[5]

    # Third rule: landmark and garden (substitution effect)
    if location_vector[7] == 1 and location_vector[16] == 1:
        utility -= 0.1
    
    return utility
