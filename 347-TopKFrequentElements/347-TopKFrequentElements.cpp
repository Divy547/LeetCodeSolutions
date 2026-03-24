// Last updated: 3/24/2026, 11:02:45 PM
1class Solution {
2public:
3    vector<int> topKFrequent(vector<int>& nums, int k) {
4        unordered_map<int, int> hashMap;
5        vector<vector<int>> buckets(nums.size() + 1);
6        vector<int> ans;
7        for(int i = 0; i < nums.size(); i++){
8            hashMap[nums[i]]++;
9        }
10        for(auto i : hashMap){
11            buckets[i.second].push_back(i.first);
12        }
13        for(int i = buckets.size() - 1; i >= 0; i--){
14            for(auto num: buckets[i]){
15                if(ans.size() == k){
16                    return ans;
17                }
18                ans.push_back(num);
19            }
20        }
21        
22        return ans;
23    }
24    
25};