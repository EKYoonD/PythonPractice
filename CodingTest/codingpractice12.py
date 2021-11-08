from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result1 = list(permutations(data, 3))
print(result1)

result2 = list(combinations(data, 2))
print(result2)

result4= list(combinations_with_replacement(data, 2))
print(result4)

# 반드시 repeat 들어가야 함
result3 = list(product(data, repeat = 2))
print(result3)
print(len(result3))
