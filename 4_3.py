def быстрое_возведение_в_степень(основание, показатель):
    результат = 1
    while показатель > 0:
        if показатель % 2 == 1:
            результат *= основание
        основание *= основание
        показатель //= 2
    return результат

новое_основание = 3
новый_показатель = 123
быстрое_возведение_в_степень(новое_основание, новый_показатель)
