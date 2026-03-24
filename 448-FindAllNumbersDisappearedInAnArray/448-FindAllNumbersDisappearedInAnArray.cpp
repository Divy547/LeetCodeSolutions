// Last updated: 3/24/2026, 11:04:29 PM
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // v.erase(remove(v.begin(), v.end(), 2), v.end());
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                ans.push_back(i+1);
            }
        }
        return ans;
    }
};