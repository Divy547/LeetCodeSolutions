# Last updated: 10/29/2026, 9:34:22 PM
class Solution:
    def largestPrime(self, n: int) -> int:
        if n <= 1 : return 0
        isPrime = lambda x : x > 1 and all(x % i for i in range(2, int(x**0.5)+1))
        sum = 0;
        ans = 0
        for i in range(2, n+1):
            if isPrime(i):
                if sum + i > n: break
                sum += i
                if isPrime(sum):
                    ans = sum
        return ans