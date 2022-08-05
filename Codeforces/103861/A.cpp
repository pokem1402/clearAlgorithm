
// #include <iostream>
// #include <sstream>
#include <vector>
#include <cstdio>

using namespace std;

struct Node
{
    /* data */
    int min_value;
    int max_value;
    vector<int> child;
};


class Tree{
    
    public:
    Node * nodes;
   
    Tree(int n){
        nodes = new Node[n + 1];
    }
};



int dfs(Tree & tree, int i, int depth, int n){

    tree.nodes[i].min_value = depth;
    int noDesc = 0;
    for (auto x : tree.nodes[i].child){
        noDesc += dfs(tree, x, depth+1, n);
    }

    tree.nodes[i].max_value = n - noDesc;
    return noDesc + 1 ; 

}


int main(){

    int t; // Test case
    int n; // n
    int parent, child;
    vector<pair<int,int>> edge;
    // cin >> t;
    scanf("%d", &t);

    while ( t > 0 ){
        // cin >> n;
        scanf("%d", &n);
        Tree tree(n);

        for (int i=0; i<n-1; i++){
            // cin >> parent >> child;
            scanf("%d %d", &parent, &child);
            edge.push_back(make_pair(parent, child));
            }
        for (auto x : edge){
                tree.nodes[x.first].child.push_back(x.second);
        }
        dfs(tree, 1, 1, n);

        for (int i=1; i< n+1; i++){
            printf("%d %d\n", tree.nodes[i].min_value, tree.nodes[i].max_value);
            // cout<<tree.nodes[i].min_value << " " <<tree.nodes[i].max_value<<endl;
        }
        edge.clear();
        t--;
    }

    return 0;
}