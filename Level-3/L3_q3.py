


def sht_dst(sx, sy, maze): # Starting points (sx, sy)
    w = len(maze[0])
    h = len(maze)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]

    while arr:
        x, y = arr.pop(0)

        for i in [[1,0], [-1,0], [0,-1], [0,1]]:
          nx, ny = x + i[0], y + i[1]

          if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if maze[nx][ny] == 1 : # Skip if its a wall
                  continue
                arr.append((nx, ny)) 

    for i in board:
      print(i)
    print()
                  
    return board



def solution(maze):

  for i in maze:
    print(i)
  print()

  w = len(maze[0])
  h = len(maze)
  startToFin = sht_dst(0, 0, maze)
  finToStart = sht_dst(h-1, w-1, maze)

  ans = 2 ** (32 - 1)
  
  for i in range(h):
      for j in range(w):
          if startToFin[i][j] and finToStart[i][j]:
              ans = min(startToFin[i][j] + finToStart[i][j] - 1, ans)
  return ans



print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))