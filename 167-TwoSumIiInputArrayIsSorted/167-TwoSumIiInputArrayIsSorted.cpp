// Last updated: 8/9/2025, 2:27:05 AM
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        while(i < j){
            int total = numbers[i] + numbers[j];
            if(target == total){
                return {i + 1, j + 1};
            }else if(total < target){
                i++;
            }else{
                j--;
            }
        }
        return {};
    }
};