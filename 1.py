
def multiples():
    i = 1
    sum = 0
    while i < 1000:
        if (i % 3 == 0) or (i % 5 == 0) :
            sum = sum + i
        i += 1
    print(sum)

multiples()