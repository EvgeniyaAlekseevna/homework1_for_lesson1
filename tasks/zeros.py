# Задача №3

n1 = 6
n2 = 12


def zeros(n):
    result = 0
    while n >= 5:
        n = n // 5
        result += n
    return result


print(zeros(n1))
print(zeros(n2))


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7