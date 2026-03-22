// Last updated: 3/22/2026, 10:52:40 PM
1class Solution {
2public:
3    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
4        vector<int> copy = nums;
5        sort(nums.begin(), nums.end());
6        vector<int> ans;
7        unordered_map<int, int> hashMap;
8        for(int i = 0; i < nums.size(); i++){
9            if(hashMap.count(nums[i])){
10            }else{
11                hashMap.insert({nums[i], i});
12            }
13        }
14        for(auto it = hashMap.begin(); it != hashMap.end(); it++)
15            cout << it->first << ": " << it->second
16            << endl;
17        for(int i = 0; i < copy.size(); i++){
18            ans.push_back(hashMap[copy[i]]);
19        }
20        return ans;
21    }
22};