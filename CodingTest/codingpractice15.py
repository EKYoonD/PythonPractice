from collections import deque
from collections import Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)

counter = Counter(['red', 'red', 'red', 'blue', 'blue', 'green'])
print(counter['red'])
