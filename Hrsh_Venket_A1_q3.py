# Question 3
def longest_common_subsequence(a,b):
    m = [[0 for x in range(len(b)+1)] for y in range(len(a)+1)]
    
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])
    
    lcs = []
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        elif m[i-1][j] > m[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()
    return''.join(lcs)

print(longest_common_subsequence('ABBC', 'BDCA'))

#   - A B C B
# - 0 0 0 0 0
# B 0 0 1 1 1
# D 0 0 1 1 1
# C 0 0 1 2 2
# A 0 1 1 2 2

# from this, we can see that the longest common subsequence is BC since BB and CC are when the value increases

print(longest_common_subsequence("dsadsanfos", "dsdnsjaknjkdsandasd"))
print(longest_common_subsequence("jbaudooNSLADKSANKDLSAKJNkflssakdnasds", "dNJBUISAIBINKDLSANMDLSAHDIOSIhDKOASDW"))