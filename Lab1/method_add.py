from Lab1.calculate_cost import calculate_cost


def add_algorithm(c, T):
    m = len(c)
    best_initial = min(range(m), key=lambda i: calculate_cost({i}, c, T))
    current_set = {best_initial}
    curr_cost = calculate_cost(current_set, c, T)

    while len(current_set) < m:
        best_candidate = None
        best_cost = curr_cost

        unopened = [i for i in range(m) if i not in current_set]
        for candidate in unopened:
            trial_set = current_set | {candidate}
            cost_val = calculate_cost(trial_set, c, T)
            if cost_val < best_cost:
                best_cost = cost_val
                best_candidate = candidate

        if best_candidate is not None:
            current_set.add(best_candidate)
            curr_cost = best_cost
        else:
            break

    z = [1 if i in current_set else 0 for i in range(m)]
    return z, curr_cost