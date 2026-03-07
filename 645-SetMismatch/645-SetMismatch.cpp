// Last updated: 3/7/2026, 1:47:50 PM
1class Solution {
2public:
3    vector<int> findErrorNums(vector<int>& nums) {
4        vector<int> hashMap;
5        vector<int> ans;
6        for(int i = 0; i <= nums.size(); i++){
7            hashMap.push_back(0);
8        }
9        for(int i = 0; i < nums.size(); i++){
10            hashMap[nums[i]]++;
11        }
12        for(int i = 1; i <= nums.size(); i++){
13            if(hashMap[i] == 2){
14                ans.push_back(i);
15                break;
16            }
17        }
18        for(int i = 1; i <= nums.size(); i++){
19            if(hashMap[i] == 0){
20                ans.push_back(i);
21                break;
22            }
23        }
24        return ans;
25    }
26};