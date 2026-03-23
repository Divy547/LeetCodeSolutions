// Last updated: 3/23/2026, 10:55:11 AM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        if(s.length() != t.length()){
5            return false;
6        }
7        // Approach : HashMaps
8        // unordered_map<char, int> hashMap;
9
10        // for(int i = 0; i < s.length(); i++){
11        //     if(!hashMap.count(s[i])){
12        //         hashMap.insert({s[i], 1});
13        //     }else{
14        //         hashMap[s[i]]++;
15        //     }
16        // }
17        
18        // for(int i =0; i < t.length(); i++){
19        //     cout<<t[i]<<" ";
20        //     if(!hashMap.count(t[i])){
21        //         return false;
22        //     }else{
23        //         hashMap[t[i]]--;
24        //     }
25        // }
26        // for(auto i : hashMap){
27        //     cout << i.first << ": " << i.second<< endl;
28        // }
29        // for(auto i : hashMap){
30        //     if(i.second != 0){
31        //         return false;
32        //     }
33        // }
34        // return true;
35        
36        // Approach: Sorting
37        sort(s.begin(), s.end());
38        sort(t.begin(), t.end());
39        cout<<s<<" "<<t;
40        if(!s.compare(t)){
41            return true;
42        }else{
43            return false;
44        }
45    }
46};