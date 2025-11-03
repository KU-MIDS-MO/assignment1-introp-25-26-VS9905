def sum_of_cubes_even(n):
    if type(n) != int or n < 0 :
        return -1

    if n > 2000:
        print("Warning!: n is more than 2000")

    final = 0.0
    for i in range(0, n+1, 2):
        final += i ** 3

    return float(final)

print(sum_of_cubes_even(10))




