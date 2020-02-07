def choose_best_sum(t, k, ls):
    from itertools import combinations
    best = 0
    for subset in combinations(ls, k):
        distance = sum(subset)
        if distance <= t:
            best = max(best, distance)
    if best != 0:
        return best
