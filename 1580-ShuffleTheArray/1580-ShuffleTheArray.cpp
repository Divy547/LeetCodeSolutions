// Last updated: 3/22/2026, 10:33:32 PM
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        int i = 0, j = n;
        while(i < n && j < 2*n){
            ans.push_back(nums[i]);
            ans.push_back(nums[j]);
            i++;
            j++;
        }
        return ans;

    }
};