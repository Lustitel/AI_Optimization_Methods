from Lab1.calculate_cost import calculate_cost

def drop_algorithm(c, T):
    m = len(c)
    current_set = set(range(m))
    curr_cost = calculate_cost(current_set, c, T)

    while len(current_set) > 1:
        best_candidate = None
        best_cost = curr_cost

        for candidate in sorted(current_set):
            trial_set = current_set - {candidate}
            cost_val = calculate_cost(trial_set, c, T)
            if cost_val < best_cost:
                best_cost = cost_val
                best_candidate = candidate

        if best_candidate is not None:
            current_set.remove(best_candidate)
            curr_cost = best_cost
        else:
            break

    z = [1 if i in current_set else 0 for i in range(m)]
    return z, curr_cost