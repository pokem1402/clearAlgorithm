from collections import deque

RY, RX, BY, BX = 0, 1, 2, 3

# Red ball 과 Blue Ball를 찾는 함수
# board에서 공의 좌표를 획득한 뒤에, board에서부터 공을 지우는 함수
# board에서 공을 지우는 이유는 bfs의 모든 과정에서 board를 재활용하기 위함이다.


def find_RandB(board):
	#공의 좌표는 적색 공의 좌표 y,x 그리고 청색 공의 y,x로 구성된다.
    ball = [-1, -1, -1, -1]
    for y, line in enumerate(board):
        if 'R' in line:
            x = line.index('R')
            ball[:2] = [y, x]
            # 공을 보드로부터 지우기
            board[y][x] = '.'
        if 'B' in line:
            x = line.index('B')
            ball[2:] = [y, x]
            # 공을 보드로부터 지우기
            board[y][x] = '.'
    return ball

# board와 red ball, blue ball, 방향을 입력하면 해당 방향으로 이동시키는 함수
# direction과의 내적으로 blue ball과 red ball 중 작은 값이 먼저 굴러간다.
# 따라서 먼저 굴러갈 공을 먼저 굴리고나서 그 다음 공을 굴리면 된다.
# 먼저 굴린 공은 같은 방향에서 늦게 굴린 공을 만나지 않고, 늦게 굴린 공은 먼저 굴린 공의 위치를 참고하므로
# 다음 위치를 참조할 때는 빈 공간인가 아닌가만 확인하면 된다.


def toward(board, ball, direction):

    # 빈 보드에 공을 놓는다.
    board[ball[RY]][ball[RX]] = 'R'
    board[ball[BY]][ball[BX]] = 'B'

    # 이동 방향에 대한 벡터를 구한다.
    dy, dx = direction

    # 판의 높이와 너비를 구해준다.
    h, w = len(board), len(board[0])

    # 적색 공과 청색 공이 도착한 경우 각각 플래그를 세운다.
    # 각각 플래그가 존재하는 이유는 청색 공이 목적지에 도달했다면, 적색 공이 목적지에 도달한 경우라도 해당 움직임은 고려하지 않아야하므로
    red_on_hole = False
    blue_on_hole = False

    # 공과 방향에 대한 내적
    # 방향 벡터와의 내적 결과 값이 큰 쪽이 해당 벡터 방향으로 멀리 있는 쪽.
    # 멀리 있는 쪽이 이동 결과 같거나 더 먼쪽에 위치함
    # 달리 해석하면 방향 벡터로부터 가장 먼 공을 먼저 이동하고 그 다음 공을 이동하면됨
    # 따라서 내적 값이 큰 공을 먼저 이동하고 그 다음 공을 이동하면됨
    # 정리하면 x1x2+y1y2이 큰 값을 먼저 이동하면 됨.
    # 반대로 코드에서는 -x1x2-y1y2이 작은 값을 먼저 이동시킴

    def dot(x, y): return - x[0]*y[0] - x[1]*y[1]

    # 내적의 결과 값이 작은 공을 먼저 굴리고, 나머지 공을 다음에 굴린다.
    ball_order = [[RY, RX], [BY, BX]] if dot(ball[:2], direction) < dot(
        ball[2:], direction) else [[BY, BX], [RY, RX]]

    # 움직임 체크하기 위한 flag
    moved = False

    # 공 순서에 따라 공을 굴린다.
    for Y, X in ball_order:
        while True:
            # 편의를 위해
            y, x = ball[Y], ball[X]
            # 다음 이동이 보드 내에서 적법한 경우.
            if (0 < y+dy) and (y+dy < h-1) and (0 < x+dx) and (x+dx < w - 1):

                # 적법한 다음 지역의 정보를 확인
                next_point = board[y+dy][x+dx]

                # 목적지인 경우
                if next_point == 'O':
                    # 적색 공이라면
                    if Y == RY:
                        red_on_hole = True
                        # 공이 빠졌으니 제거
                        board[ball[RY]][ball[RX]] = '.'
                        break
                    # 청색 공이라면
                    else:
                        # 청색 공이 빠지면 무조건 실패이기 때문에 빠져서 빨간공이 빠지는지 확인 하지 않아도됨
                        blue_on_hole = True
                        break
                # 빈 공간인 경우
                elif next_point == '.':

                    # 움직임 체크
                    moved = True
                    # 공과 빈 공간의 값을 스왑한다.
                    board[y][x], board[y+dy][x +
                                             dx] = board[y+dy][x+dx], board[y][x]
                    # 공의 위치 값을 변경한다.
                    ball[Y], ball[X] = y+dy, x+dx
                # 목적지도 아니고 빈 공간도 아닌 경우
                else:
                    break
            # 적법한 이동 가능 지역이 아닌 경우
            else:
                break

    # 보드에서 공 회수
    # 적색 공이 hole에 도달한 경우 이미 제거하였음
    if red_on_hole == False:
        board[ball[RY]][ball[RX]] = '.'
    board[ball[BY]][ball[BX]] = '.'

    return ball, red_on_hole, blue_on_hole, moved


def bfs(board, ball_init):

    # queue 선언
    q = deque()

    # 게임 상태 저장하는 리스트
    visited = []

    # ball 초기 위치와 이동 거리 0 삽입
    q.append([ball_init, 0])

    # 방향 정의
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

    # q가 빌때까지 반복
    while q:

        #ball과 count 얻기
        ball, cnt = q.popleft()

        # 각 방향 마다 반복
        for d in dir:
            # print(ball, q, d)
            ball_next, red_on_hole, blue_on_hole, moved = toward(
                board, ball.copy(), d)
            # 만약 청색 공이 빠졌다면 무시
            if blue_on_hole:
                continue
            # 만약 청색 공이 빠지지 않고 적색 공이 빠졌다면 리턴
            if red_on_hole:
                return cnt + 1

            # 움직였고, 한번도 이 상태에 놓인적이 없다면 q에 넣고 해당 상태 저장
            if moved and (ball_next not in visited):

                # 이동 카운트가 10번이 되었다면 넣지 않음
                if cnt + 1 < 10:
                    q.append([ball_next, cnt+1])
                    visited.append(ball_next)
    else:
        return -1


n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

ball_init = find_RandB(board)
print(bfs(board, ball_init))
