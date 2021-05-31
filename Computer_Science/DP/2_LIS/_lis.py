# algorithm to fine the number of elements in longest increasing series.
# Give a list
# simple dynamic method is:
# => 1.start from a node
# -> 2.list all possible ways to reach it and add them to a list
# -> 3.repeate 1 and to untill all nodes reached
# -> 4.in the way you are adding all possible ways to reach from subproblem
# -> 5.Maximum of all the reachable paths is the longest increasing series

def n_lis(A):
    L = [1] * (len(A))
    for i in range(1, len(L)):
        subproblems = [L[k] for k in range(i) if A[k] <= A[i]]
        L[i] = 1+max(subproblems, default=0)

    return max(L, default=0)

def lis(A):
    L = [1] * len(A)
    SEQ = {}
    for i in range(1, len(L)):
        SEQ[i] = []
        subproblems = []
        for k in range(0, i):
            if A[k] <= A[i]:
                subproblems.append(L[k])
                SEQ[i].append([A[k], L[k]])

        L[i] = 1+max(subproblems, default=0)

    return (max(L, default=0), SEQ)
