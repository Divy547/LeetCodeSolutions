// Last updated: 3/23/2026, 12:05:58 PM
1class Solution {
2public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        unordered_map<string, vector<string>> hashMap;
5        vector<vector<string>> ans;
6        for (int i = 0; i < strs.size(); i++) {
7            string temp = strs[i];       
8            sort(temp.begin(), temp.end()); 
9            hashMap[temp].push_back(strs[i]);
10        }
11
12
13        for (auto &i : hashMap) {
14            ans.push_back(i.second);
15        }
16        return ans;
17    }
18};