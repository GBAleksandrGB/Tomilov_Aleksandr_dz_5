src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_unique = set()
src_repeated = set()

for num in src:
    if num in src_repeated:
        continue
    if num in src_unique:
        src_repeated.add(num)
        src_unique.discard(num)
        continue
    else:
        src_unique.add(num)

print([num for num in src if num in src_unique])
