// Last updated: 4/1/2026, 11:25:43 AM
1class Solution {
2public:
3    int maxFrequencyElements(vector<int>& nums) {
4        unordered_map<int , int> hashMap;
5        for(int i = 0; i < nums.size(); i++){
6            hashMap[nums[i]]++;
7        }
8        int maxCount = 0;
9        int count = 0;
10        for(auto x : hashMap){
11            cout<<x.first<<": "<<x.second<<endl;
12            if(x.second > maxCount){
13                maxCount = x.second;
14            }
15        }
16
17        for(auto x : hashMap){
18            if(x.second == maxCount){
19                count += x.second;
20            }
21        }
22
23        return count;
24    }
25};