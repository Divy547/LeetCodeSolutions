// Last updated: 3/26/2026, 1:08:45 AM
1class Solution {
2public:
3    int longestConsecutive(vector<int>& nums) {
4        set<int> hashSet;
5        int longest = 0;
6        for(int i = 0; i < nums.size(); i++){
7            hashSet.insert(nums[i]);
8        }
9        for (auto x : hashSet){
10            int length = 1;
11            int curr = x;
12            if(!hashSet.count(x - 1)){
13                while (hashSet.count(curr + 1)){
14                    curr++;
15                    length++;
16                }
17            }
18            longest = max(longest, length);
19        }
20        return longest;
21    }
22};