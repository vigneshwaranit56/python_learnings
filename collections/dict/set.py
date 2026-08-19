nums = [1,1,1,2,2,3,3,3]

seen = set()


for x in nums:
    if x in seen:
        print(f"duplicate no {x}")

    seen.add(x)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}



print(f"union {a | b} {a.union(b)}")
print(f"intersection {a & b} {a.intersection(b)}")
print(f"difference {a - b} {a.difference(b)} ")
print(f"symmetric difference {a ^ b} {a.symmetric_difference(b)}")

print(f"a is super set of b {a.issuperset(b)} ")
print(f"a is sub set of b {a.issubset(b)} ")
print(f"a is subset of b {a.isdisjoint(b)} ")