import numpy as np

never = np.array([0 for x in range(5)])
once = np.array([1 for x in range(8)])
twice = np.array([2 for x in range(4)])
three = np.array([3 for x in range(3)])

total = np.concatenate((never, once, twice, three), axis=None)

print(np.mean(total))

