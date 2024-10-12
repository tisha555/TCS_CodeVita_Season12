import math
from collections import deque


def is_triangle(x):
    n = (-1 + math.sqrt(1 + 8 * x)) / 2.0
    return n.is_integer()


def calculate_labor_cost(weights, N, K):
    queue = deque(weights)
    cons_unshifted = 0
    curr_max = None
    shifted = []

    while cons_unshifted < K:
        
        cycle = [queue.popleft() for _ in range(min(N, len(queue)))]
        
       
        while len(cycle) > 1:
            a = cycle.pop(0)
            b = cycle.pop(0)
            if a < b:
                shifted.append(a)
                queue.append(a)
                cycle.insert(0, b)  
            else:
                shifted.append(b)
                queue.append(b)
                cycle.insert(0, a)  

        
        last_box = cycle[0]

        
        if curr_max == last_box:
            cons_unshifted += 1
        else:
            cons_unshifted = 1  
            curr_max = last_box

        
        queue.appendleft(last_box)

    
    labor_cost = sum(w for w in shifted if not is_triangle(w))
    return labor_cost


if __name__ == "__main__":
    weights = list(map(int, input().split()))
    N, K = map(int, input().split())
    result = calculate_labor_cost(weights, N, K)
    print(result, end = '')
