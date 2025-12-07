# Last updated: 12/7/2025, 8:29:52 AM
1class Solution:
2    def largestPrime(self, n: int) -> int:
3        if n <= 1 : return 0
4        isPrime = lambda x : x > 1 and all(x % i for i in range(2, int(x**0.5)+1))
5        sum = 0;
6        ans = 0
7        for i in range(2, n+1):
8            if isPrime(i):
9                if sum + i > n: break
10                sum += i
11                if isPrime(sum):
12                    ans = sum
13        return ans