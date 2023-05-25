# Задача №2

int32_1 = 2149583361
int32_2 = 32
int32_3 = 0


def int32_to_ip(int32):
    d0 = int(int32 / 256 / 256 / 256)
    d1 = int((int32 - (d0 * 256 ** 3)) / 256 / 256)
    d2 = int((int32 - (d0 * 256 ** 3) - (d1 * 256 ** 2)) / 256)
    d3 = int32 - (d0 * 256 ** 3) - (d1 * 256 ** 2) - (d2 * 256)
    return f"{d0}.{d1}.{d2}.{d3}"


print(int32_to_ip(int32_1))
print(int32_to_ip(int32_2))
print(int32_to_ip(int32_3))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
