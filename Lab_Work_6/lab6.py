def min_beer_types(N: int, B: int, preferences_str: str) -> int:
    preferences_str = preferences_str.replace(" ", "")

    if len(preferences_str) != N * B:
        raise ValueError("Невірна довжина рядка вподобань")

    beer_masks = [0] * B
    for i in range(N):
        for j in range(B):
            if preferences_str[i * B + j] == 'Y':
                beer_masks[j] |= (1 << i)

    employee_options = []
    for i in range(N):
        liked = []
        for j in range(B):
            if beer_masks[j] & (1 << i):
                liked.append(beer_masks[j])
        if not liked:
            return -1
        employee_options.append(liked)

    target = (1 << N) - 1
    best_count = B
    memo = {}

    emp_order = sorted(range(N), key=lambda x: len(employee_options[x]))

    def dfs(uncovered: int, current_count: int):
        nonlocal best_count

        if uncovered == 0:
            best_count = min(best_count, current_count)
            return

        if current_count >= best_count - 1:
            return

        if uncovered in memo and memo[uncovered] <= current_count:
            return
        memo[uncovered] = current_count

        next_emp = -1
        for i in emp_order:
            if uncovered & (1 << i):
                next_emp = i
                break

        for b_mask in employee_options[next_emp]:
            dfs(uncovered & ~b_mask, current_count + 1)

    dfs(target, 0)
    return best_count