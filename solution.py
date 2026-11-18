import graphlib

def solve(value):
    return list(graphlib.TopologicalSorter(value).static_order())
