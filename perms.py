from itertools import permutations


x = [''.join(p) for p in set(permutations("aabb"))]


print(x)
