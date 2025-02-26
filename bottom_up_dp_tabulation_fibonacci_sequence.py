# DP Tabulation Example: Fibonacci Sequence
# Time complexity: O(n)
# Space complexity: O(1)

# Define function
def fib(n):
  n = abs(n)
# Account for edge case of n <= 1
  if n <= 1:
    return n  
# Start with base cases
  a, b = 0, 1
# Build up to current nth number
  for _ in range(2,n+1): 
    a, b = b, a + b
# Return
  return b

# Test
print(fib(10))
