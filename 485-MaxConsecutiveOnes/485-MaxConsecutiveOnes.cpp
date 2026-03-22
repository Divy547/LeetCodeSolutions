// Last updated: 3/22/2026, 10:34:08 PM
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxNums = 0, curr = 0;
        for(int x: nums){
            if(x == 1){
                curr++;
            }else{
                curr = 0;
            }
            maxNums = max(curr, maxNums);
        }
        return maxNums;
    }
};