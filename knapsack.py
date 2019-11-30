

class item:
    def __init__(self, size, value):
        self.size = size
        self.value = value

class record:
    def __init__(self, value, index, selected, parent):
        self.value = value
        self.index = index
        self.selected = selected
        self.parent = parent



# This is a practice which remembers too many things -- not the best code.
# In principle, one can just remember record.value (and thus no need of record class). And using whether the value changes to decide whether the item is taken.
def knapsack_1(S, item_array):
    memo = {}
    items = []
    for i in item_array:
        items.append(item(i[0], i[1]))

    def DP(S, k):
        if (S, k) not in memo:
            if k<0:
                memo[S, k] = record(0, k, None, None)
            elif S-items[k].size < 0 or DP(S, k-1).value > DP(S-items[k].size, k-1).value + items[k].value:
                memo[S, k] = record(DP(S, k-1).value, k, False, (S, k-1))
            else:
                memo[S, k] = record(DP(S-items[k].size, k-1).value + items[k].value, k, True, (S-items[k].size, k-1))
        return memo[S, k]

    run = DP(S, len(items) - 1)
    print("Total value = ", run.value)

    selected = []
    while run.parent is not None:
        if run.selected:
            selected.append(run.index)
        run = memo[run.parent]
    print("Selected items: ", selected[::-1])
       

# This should be well-written
def knapsack_2(S, item_array):
    memo = {}
    items = [item(i[0], i[1]) for i in item_array]
    def DP(S, k):
        if S < 0: return float('-inf')
        if (S, k) not in memo:
            memo[(S, k)] = max(DP(S, k-1), DP(S-items[k].size, k-1) + items[k].value) if k>=0 else 0
        return memo[(S, k)]
    
    print("Total value = ", DP(S, len(items)-1))
    remaining = S
    for k in reversed(range(len(items))):
        if DP(remaining, k) != DP(remaining, k-1):
            print("Taken: ", k)
            remaining -= items[k].size


# Using lru_cache to cache instead of memorizing by hand
from functools import lru_cache
def knapsack_3(S, item_array):
    items = [item(i[0], i[1]) for i in item_array]

    @lru_cache(maxsize=None)
    def DP(S, k):
        if S < 0: return float('-inf')
        return max(DP(S, k-1), DP(S-items[k].size, k-1) + items[k].value) if k>=0 else 0
    
    print("Total value = ", DP(S, len(items)-1))
    remaining = S
    for k in reversed(range(len(items))):
        if DP(remaining, k) != DP(remaining, k-1):
            print("Taken: ", k)
            remaining -= items[k].size
    print(DP.cache_info())

knapsack = knapsack_3
knapsack(8, [[1, 15], [5, 10], [3, 9], [4, 5]])
knapsack(3, [[2,2],[1,1],[2,2]])
knapsack(165, [[23,92],[31,57],[29,49],[44,68],[53,60],[38,43],[63,67],[85,84],[89,87],[82,72]])