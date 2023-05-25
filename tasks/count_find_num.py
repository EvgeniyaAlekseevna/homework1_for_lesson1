# Задача №5
import math

primesL1 = [2, 5, 7]
limit1 = 500


def count_find_num(primesL, limit):
    composition = math.prod(primesL)

    def recursion(composition, primesL, limit):
        if composition > limit:
            return []
        meanings = [composition]
        for item in primesL:
            composition_new = composition * item
            meanings += recursion(composition_new, primesL, limit)
        meanings = list(set(meanings))
        return meanings

    result = recursion(composition, primesL, limit)
    if result:
        return [len(result), max(result)]
    return []


print(count_find_num(primesL1, limit1))
print(count_find_num(primesL1, limit1) == [5, 490])


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []