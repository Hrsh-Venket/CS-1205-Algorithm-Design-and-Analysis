# Question 2
# 2.1
def matrix_chain_order(p):
    n = len(p)
    m = [[0 for x in range(n)] for y in range(n)]
    s = [[0 for x in range(n)] for y in range(n)]
    for l in range(2,n+1):
        for i in range(1,n-l+1):
            j = i+l-1
            m[i][j] = 100000
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    # print optimal parenthesis
    return m, s, m[1][n-1]

# Question 2.2
p = [10, 8, 5, 15, 20, 12]
matrix_chain_order(p)

# From this, we can the sequence of parenthesis is:
# (A1A2)((A3A4)A5)
# and the output below returns m, s, and the optimal number of scalar multiplications
