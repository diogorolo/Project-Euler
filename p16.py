def prob16():
    number = 2**1000
    number_str = str(number)
    sum = 0
    for i in number_str:
        sum += int(i)
    return sum

print(prob16())
