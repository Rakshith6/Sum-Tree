import Sum_Tree as ST
import numpy as np
import matplotlib.pyplot as plt
import random

A = np.arange(12) # array of priorities
# random.shuffle(A)
sum_tree = ST.Sum_Tree(len(A)) # initialize sum tree

sum_tree.priorities = A # set priority data in sum tree

sum_tree.update_allLeaves() # update the leaves with the priority values. Runs values up the tree as well

# Update a leaf to check if the change is propagating
leaf_no = 2
leaf_value = 6
sum_tree.update_leaf(leaf_no,leaf_value)

# Return priority for a random sum value
sum = np.random.uniform(0,sum_tree.tree_nodes[0])
priority_index,priority = sum_tree.get_priority(sum,0)

# Generate frequency for priorities - Higher priorities should be picked at greater frequency
priority_frequency = np.zeros(len(A))
sample_sums = np.linspace(0,sum_tree.tree_nodes[0],100000)
for sum in sample_sums:
    priority_index, priority = sum_tree.get_priority(sum, 0)

    priority_frequency[priority_index]+=1

prob_plot = plt.subplot()
prob_plot.plot(priority_frequency/100000)
prob_plot.set_ylabel('Probability of choosing the priority')
prob_plot.set_xlabel('Priority value')
prob_plot.set_yticks(np.arange(0,1.1,0.2))
