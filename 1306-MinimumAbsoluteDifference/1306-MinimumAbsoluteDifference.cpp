// Last updated: 3/22/2026, 10:33:42 PM
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int minDiff = INT_MAX;
        int i = 0;
        int j = 1;
        vector<vector<int>> ans;
        while(j < arr.size()){
            int diff = abs(arr[j] - arr[i]);
            if(diff < minDiff){
                minDiff = diff;
                ans.clear();
                ans.push_back({arr[i], arr[j]});
            }else if(diff == minDiff){
                ans.push_back({arr[i], arr[j]});
            }
            i++;
            j++;
        }
        return ans;
    }
};