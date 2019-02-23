string = "How good is have account on StackOverflow and create new posts"


def odd(data):
    idx, el = data
    return el if idx % 2 == 0 else el + "\n"


print(" ".join(list(map(odd, list(enumerate(string.split(" ")))))))
