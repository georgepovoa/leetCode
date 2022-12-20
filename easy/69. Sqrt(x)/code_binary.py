
import time
st = time.time()


def mySqrt(x: int) -> int:
    if x==0 or x == 1:
            return x
    if x < 4 :
        return int(x/2)
    top = int(x/2)
    bottom = 0
    mid = int(top / 2)
    while (True):
        if mid ** 2 > x:
            top = mid
            mid = int((top+bottom )/ 2)
        else:
            bottom = mid
            top = top + (int((top+mid)/2))
            
            mid = int((top+bottom )/ 2)

        if ((mid + 1) ** 2 > x and (mid - 1) ** 2 < x):
            if mid ** 2 > x:

                return mid-1
            else:
                return mid

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
