// Last updated: 3/28/2026, 11:48:46 PM
1class Solution {
2public:
3    vector<int> twoSum(vector<int>& numbers, int target) {
4        int i = 0;
5        int j = numbers.size() - 1;
6        while(i < j){
7            int total = numbers[i] + numbers[j];
8            if(target == total){
9                return {i + 1, j + 1};
10            }else if(total < target){
11                i++;
12            }else{
13                j--;
14            }
15        }
16        return {};
17    }
18};