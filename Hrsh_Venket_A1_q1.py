# Question 1
# 1.1
parent = {}
rank = {}

def make_set(x):
    parent[x] = x
    rank[x] = 0

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 1.2 and 1.3
# the elements in each set are represented in brackets:
    # ie. (b) means b is in a set by itself
# the arrows represent the parent-child relationship:
    # ie. (a -> b) means a is the child of b
# the element in a set to which all arrows lead to is the root of that set
# the root represents the set
# the sets are separated by commas

make_set(1)
# (1)
make_set(2)
# (1), (2)
make_set(3)
# (1), (2), (3)
make_set(4)
# (1), (2), (3), (4)
make_set(5)
# (1), (2), (3), (4), (5)
make_set(6)
# (1), (2), (3), (4), (5), (6)
make_set(7)
# (1), (2), (3), (4), (5), (6), (7)
make_set(8)
# (1), (2), (3), (4), (5), (6), (7), (8)
make_set(9)
# (1), (2), (3), (4), (5), (6), (7), (8), (9)
make_set(10)
# (1), (2), (3), (4), (5), (6), (7), (8), (9), (10)
union(1, 2)
# (1 -> 2), (3), 4), (5), (6), (7), (8), (9), (10)
union(2, 3)
# (1 -> 2 <- 3), (4), (5), (6), (7), (8), (9), (10)
union(4, 5)
# (1 -> 2 <- 3), (4 -> 5), (6), (7), (8), (9), (10)
union(3,4)
# (4 -> 5
#       ^
#       |
#  1 -> 2 <- 3), (6), (7), (8), (9), (10)
print(find(1))
# 1's parent is 2, 2's parent is 5, so 1 returns 5 
# (1 is in the set represented by 5)
print(find(10))
# 10's parent is 10, so 10 returns 10 
# (10 is in the singleton set represented by 10)
print(find(5))
# 5's parent is 5, so 5 returns 5
# (5 is in the set it represents)