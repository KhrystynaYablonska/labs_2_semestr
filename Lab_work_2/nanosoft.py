def find_min_board(W, H, N):
    left = 0

    if W > H:
        right = N * W
    else:
        right = N * H

    while left < right:
        mid = (left + right) // 2
        count = (mid // W) * (mid // H)

        if count >= N:
            right = mid
        else:
            left = mid + 1

    return left