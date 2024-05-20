
input_a, input_b = int(input()), int(input())
result_array = list()
for num in range(input_a, input_b+1):
    if num > 1:
        prime_flag = True
        for divisor in range(2, num):
            if num % divisor == 0:
                prime_flag = False
                break
        if prime_flag:
            result_array.append(num)
    else:
        continue
print(sum(result_array))
