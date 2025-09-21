import heapq
from typing import List, Tuple

def optimal_merge(lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    if not lengths:
        return 0, []
    if len(lengths) == 1:
        return 0, []
    
    heap = lengths[:]
    heapq.heapify(heap)
    total_cost = 0
    merges = []

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost 
        merges.append((a, b, cost))
        heapq.heappush(heap, cost)

    return total_cost, merges

if __name__ == "__main__":
    example = [
        [4, 2, 6, 13],
        [11, 7, 3, 9],
        [5, 2, 14, 8],
    ]

    for ex in example:
        cost, ops = optimal_merge(ex)
        print("Login:", ex)
        print("Merge order (a, b -> a+b):")
        for a,b,c in ops:
            print(f" {a} + {b} -> {c}")
        print("Minimum cost:", cost)    
        print("-" * 30)    