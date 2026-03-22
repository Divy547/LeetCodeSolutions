// Last updated: 3/22/2026, 10:11:23 PM
1class Solution {
2public:
3    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
4        // nums.sort();
5        // vector<int> buff;
6        vector<int> ans;
7        for(int i = 0; i < nums.size(); i++){
8            int count = 0;
9            for(int j = 0; j < nums.size(); j++){
10                if(nums[i] > nums[j]){
11                    count++;
12                }
13            }
14            ans.push_back(count);
15        }
16        return ans;
17    }
18};