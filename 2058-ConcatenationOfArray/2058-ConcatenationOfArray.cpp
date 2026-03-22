// Last updated: 3/22/2026, 10:33:20 PM
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int n = nums.size();
        for(int i =0; i < 2*nums.size(); i++){
            if(i >= nums.size()){
                ans.push_back(nums[i-n]);
            }else
                ans.push_back(nums[i]);
        }
        return ans;
    }
};