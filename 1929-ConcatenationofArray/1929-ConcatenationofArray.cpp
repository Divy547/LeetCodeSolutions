// Last updated: 3/4/2026, 7:23:14 PM
1class Solution {
2public:
3    vector<int> getConcatenation(vector<int>& nums) {
4        vector<int> ans;
5        int n = nums.size();
6        for(int i =0; i < 2*nums.size(); i++){
7            if(i >= nums.size()){
8                ans.push_back(nums[i-n]);
9            }else
10                ans.push_back(nums[i]);
11        }
12        return ans;
13    }
14};