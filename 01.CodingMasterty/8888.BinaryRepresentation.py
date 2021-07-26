def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        print(n)
        n >>= 1
    return count


# Program to test function countSetBits */
i = 9
print(countSetBits(i))



print([0]*4)