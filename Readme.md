# Sum tree data structure

Created for the purpose of sampling from discrete priority distributions stochastically. A priority is associated with each sample point and we can sample
stochastically according to the sample priorities.

## Sum tree class

1. update_leaf - updates the priority value on the leaf and propagates the change in priority value for that leaf up the tree.
2. update_tree - propagates the change in priority value of a leaf up the tree
3. get_priority - returns a priority given a sum value
4. update_allLeaves - runs update_leaf for all the leaves. Can be used to set all leaf priorities at once and propagate them 

## Sum tree test script

Originally, created to debug the Sum tree class. Generating frequency of choosing priority samples using large number of sum values confirms the
working of the sum tree as intended.
