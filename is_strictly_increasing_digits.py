def is_strictly_increasing_digits(n):
    if type(n) != int or n < 0:
        return -1

    d = str(n)
    for i in range(len(d)-1):
        if d[i] >= d[i+1]:
            return False
    return True



