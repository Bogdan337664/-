import itertools

def комбинации(слово: str):
    набор_комбинаций = set()
    for длина in range(1, len(слово) + 1):
        for комбинация in itertools.permutations(слово, длина):
            набор_комбинаций.add(''.join(комбинация))
    return набор_комбинаций

print(комбинации("здравствуйте"))
