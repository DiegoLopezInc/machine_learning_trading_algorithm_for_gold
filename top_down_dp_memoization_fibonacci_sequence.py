# DP Memoization Example: Fibonacci Sequence
# Time complexity O(n)
# Space complexity O(N)

# Define a recursive function to calculate the nth Fibonacci number
def fib(n, memo={}):
    n = abs(n) # Ensure that n is positive
    if n <= 1: 
        return n
# Check the cache and return if the number is already calculated
    if n in memo:
        return memo[n]
# Otherwise, calulate the number and store it in the cache
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
# Return the calculated number
    return memo[n]

# Test
print(fib(10))
