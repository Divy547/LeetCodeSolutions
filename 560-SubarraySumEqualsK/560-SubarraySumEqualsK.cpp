// Last updated: 3/26/2026, 6:24:29 PM
1class Solution {
2public:
3    int subarraySum(vector<int>& nums, int k) {
4        unordered_map<int, int> hashMap;
5        hashMap[0] = 1;
6        int count = 0;
7        int prefixSum = 0;
8        for(int i = 0; i < nums.size(); i++){
9            prefixSum += nums[i];
10            if(hashMap.count(prefixSum - k)){
11                count += hashMap[prefixSum - k];
12            }
13            hashMap[prefixSum]++;
14        }
15        return count;
16    }
17};