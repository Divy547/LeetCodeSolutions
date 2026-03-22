// Last updated: 3/22/2026, 10:33:36 PM
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // nums.sort();
        // vector<int> buff;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++){
            int count = 0;
            for(int j = 0; j < nums.size(); j++){
                if(nums[i] > nums[j]){
                    count++;
                }
            }
            ans.push_back(count);
        }
        return ans;
    }
};