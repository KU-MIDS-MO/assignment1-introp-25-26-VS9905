def count_digits_greater_than(n, t):
    count = 0

    if type(n) != int or n < 0 :
        return -1

    if type(t) != int or t < 0 or t > 9:
        return -1

    for d in str(n):
        if int(d) > t :
            count += 1

    return count



