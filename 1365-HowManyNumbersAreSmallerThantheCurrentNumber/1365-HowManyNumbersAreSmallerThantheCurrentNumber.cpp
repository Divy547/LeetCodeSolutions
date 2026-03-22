// Last updated: 3/22/2026, 11:45:02 PM
1class Solution {
2public:
3    vector<int> findDisappearedNumbers(vector<int>& nums) {
4        sort(nums.begin(), nums.end());
5        // v.erase(remove(v.begin(), v.end(), 2), v.end());
6        vector<int> ans;
7
8        for (int i = 0; i < nums.size(); i++) {
9            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1;
10        }
11        for (int i = 0; i < nums.size(); i++) {
12            if (nums[i] > 0) {
13                ans.push_back(i+1);
14            }
15        }
16        return ans;
17    }
18};