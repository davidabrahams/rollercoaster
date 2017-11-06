from itertools import permutations

def is_rollercoaster(A):
    for i in range(len(A) - 2):
        if (A[i] < A[i+1]) == (A[i+1] < A[i + 2]):
            return False
    return True



for N in range(1, 8):
    all_perms = permutations([i + 1 for i in range(N)])
    c = 0
    coasters = []
    for p in all_perms:
        if is_rollercoaster(p):
            c += 1
            coasters.append(p)
    print "N:%i, coasters:%i" % (N, c)
    # for co in coasters:
    #     print co
