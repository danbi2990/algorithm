
dx = (1, 1, 1, 0, -1, -1, -1, 0, 2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 0, -1, -1, -1, 0, 1, 1, -1, -2, -2, -1, 1, 2, 2, 1)
ways = [[[0 for z in range(55)] for x in range(100)] for y in range(100)]


# ex: (size=3, start=(0,0), end=(0,0), num_moves=2)
class ChessMetric:
    def howMany(self, size, start, end, num_moves):
        sx, sy, ex, ey = start[0], start[1], end[0], end[1]
        ways[sy][sx][0] = 1
        for i in range(1, num_moves + 1):
            for x in range(size):
                for y in range(size):
                    for j in range(16):
                        nx, ny = x + dx[j], y + dy[j]
                        if(nx < 0 or ny < 0 or nx >= size or ny >= size):
                            continue
                        ways[ny][nx][i] += ways[y][x][i - 1]
        return ways[ey][ex][num_moves]

obj = ChessMetric()
print(obj.howMany(100, (0, 0), (0, 99), 50))
