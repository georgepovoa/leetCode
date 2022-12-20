import time
st = time.time()


def mySqrt(x: int) -> int:

    i = 10
    closer = 2147483648
    closer_i = 0

    while (True):
        check = i**2
        if check > x:

            break
        i += 10

    for i in range(i-10, i+1):
        check = i**2 - x

        if check < 0:
            check = check * -1

        if check < closer:
            closer = check
            closer_i = i

    if closer_i ** 2 > x:
        closer_i -= 1

    return closer_i


print(mySqrt(3))

print(mySqrt(50))

print(mySqrt(1000))

print(mySqrt(5000))

print(mySqrt(100000))

print(mySqrt(500000))

print(mySqrt(10000000))

print(mySqrt(50000000))

print(mySqrt(5000000000))

print(mySqrt(500000000000))


print(mySqrt(50000000000000))


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
