// Last updated: 12/4/2025, 5:25:57 PM
1class Solution {
2public:
3    int minElement(vector<int>& nums) {
4        int ans = INT_MAX;
5        for( int x : nums){
6            int s = 0;
7            while( x > 0){
8                int a = x % 10;
9                s+=a;
10                x = x / 10;
11            }
12            ans = min(ans, s);
13        }
14        return ans;
15    }
16};