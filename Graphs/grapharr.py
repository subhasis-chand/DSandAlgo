mat = [[0 for _ in range(4)] for _ in range(4)]

edges = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (2, 3, 1)]
print(mat)

for edge in edges:
    u, v, w = edge
    mat[u][v] = w

print("Adjacency Matrix:")
for row in mat:
    print(row)

# adjacency list
edges2 = [(0, 1), (0, 2), (1, 2), (2, 3)]

adj_list = [[] for _ in range(4)]
for edge in edges2:
    u, v = edge
    adj_list[u].append(v)

print("Adjacency List:", adj_list)
# for i in range(len(adj_list)):
#     neighbors = adj_list[i]
#     print(f"{i}: {neighbors}")