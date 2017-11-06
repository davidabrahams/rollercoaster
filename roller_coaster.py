
def get_A_n_x(n, x, A):
    if n == 1 and x == 1:
        A[1][1] = 1
    if A[n][x] is not None:
        return A[n][x]
    s = 0
    for k in range(1, x + 1):
        s += get_A_n_x(n-1, n - k, A)
    A[n][x] = s
    return s

answers = []
print "A_n,x is num roller coasters of [1, 2, ..., n] where first num is <= x, and first slope is increasing"
for i in range(1, 9):
    if i == 1:
        answers.append(1)
        continue
    A = [[None] * (i + 1) for _ in range(i + 1)]
    total_rollercoasters = 2 * get_A_n_x(i, i, A)
    answers.append(total_rollercoasters)

for i in range(1, 8):
    print 'A[%i][1]: %i' % (i, A[i][1])

for i, x in enumerate(answers):
    print i + 1, x
