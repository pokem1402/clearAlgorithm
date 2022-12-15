from copy import deepcopy
from collections import deque

# 방향 벡터와 리스트 순서를 합친 튜플의 나열
# 순서대로 down, up, left, right
# 내부의 값 : (벡터 y값, x값, y 리스트 방향, x 리스트 방향)
VY, VX, Y_LIST_OD, X_LIST_OD = 0, 1, 2, 3
dir = [(1, 0, -1, 1),  # down
       (-1, 0, 1, 1),  # up
       (0, -1, 1, 1),  # left
       (0, 1, 1, -1)]  # right

# 보드 내의 숫자를 이동시키는 함수
# 문제의 <그림 14> -> <그림 15>를 보면 알 수 있듯이 보드 내의 이동은 방향 벡터 기준으로 가장 먼쪽의 요소들부터 움직이면 된다.
# 해당 방향의 가장자리 부분은 이동시킬 필요가 없다.
# 순서는 진행방향의 반대 순서로 진행하되, 수직 성분의 순서는 어떤 순서로부터 이동해도 상관 없다.
def toward(_board, direction):

    # 보드판을 copy
    board = deepcopy(_board)

    # 보드판의 가로, 세로
    n = len(board)

    # 합침 여부를 기록하는 보드 판을 하나 만든다
    bs = [[False for _ in range(n)] for _ in range(n)]

    # 이동 방향에 대한 벡터 값
    dy, dx = direction[VY], direction[VX]

    # 보드를 리스트 순서대로 참조해야되는지, 역방향으로 참조해야하는지에 대한 값
    list_order_y, list_order_x = direction[Y_LIST_OD], direction[X_LIST_OD]

    # 보드의 이동방향에 따라서 먼저 이동하는 숫자가 달라진다.
    # 예를 들어 왼쪽으로 이동하는 경우에는 x가 가장 작은 값들 부터 왼쪽으로 이동하여 x값이 증가되는 순서대로 이동을 시작해야한다.
    order = ["Y", "X"] if dy else ["X", "Y"]

    # Y축과 X축으로 실행될 순서의 리스트
    # Y축의 경우에 위로 이동하는 경우에는 정방향, 아래로 이동하는 경우에는 리스트가 역순으로 참조되어야 아래부터 이동되므로 -1
    # X축의 경우에는 좌로 이동하는 경우가 정방향, 우로 이동하는 경우에는 리스트를 역순으로 참조되어야 오른쪽부터 이동되므로 -1
    range_ = {"Y": list(range(n))[::list_order_y],
              "X": list(range(n))[::list_order_x]}

    # 변화의 유무를 추적하는 플래그
    changed = False

    # 이동하는 축의 가장 가장자리에 놓인 숫자는 이동할 필요가 없으므로 반복문을 수행하지 않음
    # 숫자라면 이동할 이유가 없고, 빈칸 (0) 인 경우에는 더더욱 이동할 필요가 없음
    for fst_order in range_[order[0]][1:]:
        for sec_order in range_[order[1]]:
            # 현재 위치의 좌표값
            y, x = (fst_order, sec_order) if dy else (sec_order, fst_order)

            # 현재 위치의 값이 빈 칸인 경우에는 건너뜀 (이동할 필요가 없음)
            if board[y][x] == 0:
                continue

            # 현재 위치의 값이 빈 칸이 아닌 경우
            # 숫자 값을 획득
            value = board[y][x]

            while True:
                # 이동이 적법한 경우
                if (y+dy >= 0) and (y+dy < n) and (x+dx >= 0) and (x+dx < n):
                    next_point = board[y+dy][x+dx]

                    # 다음 칸이 빈칸인 경우
                    if next_point == 0:
                        # 다음 칸과 현재 칸을 스왑
                        board[y][x], board[y+dy][x +
                                                 dx] = board[y+dy][x+dx], board[y][x]
                        bs[y][x], bs[y+dy][x+dx] = bs[y+dy][x+dx], bs[y][x]
                    # 다음 칸이 빈칸이 아니라 숫자 인 경우
                    else:
                        # 다음 칸과 현재 칸의 숫자가 같은 경우 : 병합 후 이동 재개
                        # 현재 숫자 혹은 다음 칸의 숫자 모두 한번이라도 합치지 않은 경우에만 합병
                        if (next_point == value) and (bs[y+dy][x+dx] == False) and (bs[y][x]==False):
                            board[y][x], board[y+dy][x+dx] = 0, 2*value
                            bs[y][x], bs[y+dy][x+dx] = False, True
                            value *= 2
                        # 다음 칸과 현재 칸의 숫자가 다른 경우 : 정지
                        else:
                            break

                    #좌표 이동
                    y, x = y+dy, x+dx
                    # 숫자가 이동 혹은 숫자가 병합 : 변화 발생
                    changed = True

                # 이동이 적법하지 않은 경우
                else:
                    break

    return board, max(map(max, board)), changed

# bfs
def bfs(board_init):

    # queue 생성
    q = deque()

    # 방문한 상태를 저장하는 리스트
    visited = [board_init]

    # 초기값을 queue에 넣음
    q.append([board_init, 0])

    # 최댓값을 저장하는 변수
    max_value = -1

    # q 값이 빌 때 까지 순환
    while q:

        # board와 카운터 획득
        board, cnt = q.popleft()

        # 매 방향마다 반복문 수행
        for d in dir:

            # 다음 보드 상태, 이동한 후의 최댓값, 변화 플래그
            next_board, _max, changed = toward(board, d)

            # 현재까지의 최댓값과의 비교
            max_value = max(max_value, _max)

            # 최대 횟수(5회)보다 적게 이동하였다면 이하의 행동을 수행한다.
            if cnt + 1 < 5:

                # 상태가 변화하였고, 그 상태가 이전에 있던 상태가 아니라면
                if changed and (next_board not in visited):
                    q.append([next_board, cnt + 1])
                    visited.append(next_board)

    return max_value

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

print(bfs(board))