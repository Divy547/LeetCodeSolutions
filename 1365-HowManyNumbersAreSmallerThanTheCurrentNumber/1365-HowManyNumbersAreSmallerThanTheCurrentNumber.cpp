// Last updated: 10/29/2026, 9:35:47 PM
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> copy = nums;
        sort(nums.begin(), nums.end());
        vector<int> ans;
        unordered_map<int, int> hashMap;
        for(int i = 0; i < nums.size(); i++){
            if(hashMap.count(nums[i])){
            }else{
                hashMap.insert({nums[i], i});
            }
        }
        for(auto it = hashMap.begin(); it != hashMap.end(); it++)
            cout << it->first << ": " << it->second
            << endl;
        for(int i = 0; i < copy.size(); i++){
            ans.push_back(hashMap[copy[i]]);
        }
        return ans;
    }
};