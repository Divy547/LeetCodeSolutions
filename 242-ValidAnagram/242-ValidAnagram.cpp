// Last updated: 3/23/2026, 10:50:06 AM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        if(s.length() != t.length()){
5            return false;
6        }
7        unordered_map<char, int> hashMap;
8
9        for(int i = 0; i < s.length(); i++){
10            if(!hashMap.count(s[i])){
11                hashMap.insert({s[i], 1});
12            }else{
13                hashMap[s[i]]++;
14            }
15        }
16        
17        for(int i =0; i < t.length(); i++){
18            cout<<t[i]<<" ";
19            if(!hashMap.count(t[i])){
20                return false;
21            }else{
22                hashMap[t[i]]--;
23            }
24        }
25        for(auto i : hashMap){
26            cout << i.first << ": " << i.second<< endl;
27        }
28        for(auto i : hashMap){
29            if(i.second != 0){
30                return false;
31            }
32        }
33        return true;
34    }
35};