# Задача №4
from itertools import combinations

s1 = "bbananana"


def bananas(s) -> set:
    word = "banana"
    result = set()
    for item in combinations(range(len(s)), len(s) - len(word)):
        list_item = list(s)
        for i in item:
            list_item[i] = "-"
        res = "".join(list_item)
        if res.replace("-", "") == word:
            result.add(res)
    return result


print(bananas(s1))


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                "b-a--nana", "-banan--a", "b-ana--na",
                                "b---anana", "-bana--na", "-ba--nana",
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",
                               "b--anana", "banana--", "banan--a"}
