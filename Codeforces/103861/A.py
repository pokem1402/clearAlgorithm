class Tree:
    def __init__(self, data):
        self.children = []
        self.min_value =0
        self.max_value =0
         
def dfs(v, d):
    
    v.min_value = d
    
    noDescendant = 0
    
    for child in v.children:
        noDescendant += dfs(child, d+1)
        
    v.max_value = n - noDescendant
    return noDescendant + 1
    

T = int(input()) # The number of Test case


for i in range(T):
    n = int(input())
 
    #make_graph
    vertex = [Tree(i) for i in range(n+1)]
    for j in range(n-1):
        parent, child = list(map(int, input().split()))
        vertex[parent].children.append(vertex[child])

    dfs(vertex[1], 1)
    for i in range(1, n+1):
        print(vertex[i].min_value, vertex[i].max_value)
    
    
    