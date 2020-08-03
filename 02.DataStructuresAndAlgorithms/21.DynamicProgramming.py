
#Assume fibonacii numbers starting from 0 , ie 1 1 2 3 5 8.... we want to print the nth fib number, n starts from 1 ie first


#Normal recursive version with horrible time complexity O(2^n)
def fib_recursive(n):
    if n<=2 : return 1
    else: return  fib_recursive(n-1)+fib_recursive(n-2)



#Dynamic Programming Version(with Memoization strategy). Time complexity O(n)
def fib_memoization(n, memo):
    if n  in memo:
        return memo[n]
    else:
        if(n<=2):
            return 1
        else:
            f=fib_memoization(n-1,memo)+fib_memoization(n-2,memo)
            memo[n]=f
            return f

#Dynamic Programming using bottom up upproch, ie Tabulation. Improves space complexity. Will not cause stack overflow
def fib_tabulation(n):
    if n<=2 : return 1

    fibArray={0:0,1:1,2:1}
    for i in range(3,n+1):
        fibArray[i]=fibArray[i-1]+fibArray[i-2]
    return fibArray[n]





print(fib_recursive(3)) #For heavens sake dont try with anything higher than 40!! DANGER ALERT!!
print(fib_tabulation(999)) #Best Approch, still dont try with huge numbers
print(fib_memoization(999,{})) # n>=1000 causes stack overflow

