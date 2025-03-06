OFFSET = 100000
WHITE = 1
BLACK = 2

tiles = [0] * (OFFSET * 2 + 1)
white_count = 0
black_count = 0

n = int(input())
current_position = OFFSET

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'L':
        while x > 0:
            tiles[current_position] = WHITE
            x -= 1
            if x > 0:
                current_position -= 1
    elif direction == 'R':
        while x > 0:
            tiles[current_position] = BLACK
            x -= 1
            if x > 0:
                current_position += 1

white_count = tiles.count(WHITE)
black_count = tiles.count(BLACK)

print(white_count, black_count)
