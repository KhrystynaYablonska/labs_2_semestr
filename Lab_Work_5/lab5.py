from collections import deque

def min_knight_moves(N, start, target):
    row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    col_moves = [-1, 1, 1, -1, 2, -2, 2, -2]

    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()

        if x == target[0] and y == target[1]:
            return steps

        for i in range(8):
            nx = x + row_moves[i]
            ny = y + col_moves[i]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    N = int(lines[0].split('#')[0].strip())
    start_str = lines[1].split('#')[0].strip()
    start = tuple(map(int, start_str.split(',')))
    target_str = lines[2].split('#')[0].strip()
    target = tuple(map(int, target_str.split(',')))

    result = min_knight_moves(N, start, target)

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()