def calculate_cost(open_set, c, T):
    if not open_set:
        return float('inf')
    open_cost = sum(c[i] for i in open_set)
    trans_cost = sum(min(T[i][j] for i in open_set) for j in range(len(T[0])))
    return open_cost + trans_cost