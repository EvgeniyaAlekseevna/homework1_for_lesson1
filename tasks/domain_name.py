# Задача №1

url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"
url3 = "https://www.cnet.com"


def domain_name(url):
    if "://" in url:
        url_split = url.split("://")[1]
        if "www." in url_split:
            return url_split.split("www.")[1].split(".")[0]
        else:
            return url_split.split(".")[0]
    elif "www." in url:
        return url.split("www.")[1].split(".")[0]


print(domain_name(url1))
print(domain_name(url2))
print(domain_name(url3))


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
