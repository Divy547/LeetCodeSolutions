// Last updated: 3/4/2026, 7:29:17 PM
1class Solution {
2public:
3    int findMaxConsecutiveOnes(vector<int>& nums) {
4        int maxNums = 0, curr = 0;
5        for(int x: nums){
6            if(x == 1){
7                curr++;
8            }else{
9                curr = 0;
10            }
11            maxNums = max(curr, maxNums);
12        }
13        return maxNums;
14    }
15};