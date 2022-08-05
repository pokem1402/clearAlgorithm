
Source : https://codeforces.com/gym/103861/problem/A

# A. DFS Order
> 각 테스트 별 제한 시간 : 3초.
>
> 각 테스트 별 제한 메모리 크기 : 1024mb
>
> 입출력 : standard I/O

</br>

## 문제 요약 정리

</br>

 $n$개의 node가 존재하는 rooted tree에서 아래의 pseudo-code에 의한 DFS order로 각 노드를 순회할 때, 특정 노드에 방문하는 순서의 최솟값과 최대값을 구하여라.

```
let dfs_order be an empty list

def dfs(vertex x):
    append x to the end of dfs_order.
    for (each son y of x): // sons can be iterated in arbitrary order.
        dfs(y)

dfs(root)
```

</br>

## 입력

첫 줄에는 테스트 케이스의 수를 지정하는 하나의 정수 $T \; (1 \leq T \leq 10^6)$.

각 테스트 케이스마다 (두 번째 줄 이후부터) 첫 줄에는 정수 $n \; (1 \leq n \leq 10^5)$. 그리고 이후 다음 각 $n-1$의 줄에서는 두 정수 $x, y$가 표기되며 이 때 $x$는 $y$의 parent node $( 1\leq x,y \leq n).$ 이런 두 노드들로 형성되는 간선들은 1 노드를 root로 하는 tree를 형성한다.

각 테스트 케이스에 대응하는 $n$의 총합은 $10^6$이 넘지 않는다.

## 출력

각 테스트 케이스마다, $n$개의 결과물을 각 줄마다 출력하며, 이렇게 출력하는 $i$번째 줄에는 $i$번째 노드의 방문 순서의 최솟값과 최대값을 출력한다.


## Example
---
### **input**
```
2
4
1 2
2 3
3 4
5
1 2
2 3
2 4
1 5
```
---
### **output**
```
1 1
2 2
3 3
4 4
1 1
2 3
3 5
3 5
2 5
```

</br>

# 문제 해결

## 