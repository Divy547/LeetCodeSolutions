// Last updated: 9/1/2025, 11:08:58 PM
class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        int count[101];
        for (int i = 0; i < nums.size(); i++){
            if(++count[nums[i]]>= 3){
                return false;
            }
        }
        return true;
    }
};