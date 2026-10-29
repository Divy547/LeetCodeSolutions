// Last updated: 10/29/2026, 9:34:32 PM
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