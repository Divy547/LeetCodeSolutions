// Last updated: 3/4/2026, 7:26:03 PM
1class Solution {
2public:
3    vector<int> shuffle(vector<int>& nums, int n) {
4        vector<int> ans;
5        int i = 0, j = n;
6        while(i < n && j < 2*n){
7            ans.push_back(nums[i]);
8            ans.push_back(nums[j]);
9            i++;
10            j++;
11        }
12        return ans;
13
14    }
15};