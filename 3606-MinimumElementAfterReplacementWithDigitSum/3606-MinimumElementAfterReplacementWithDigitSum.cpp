// Last updated: 3/22/2026, 10:33:13 PM
class Solution {
public:
    int minElement(vector<int>& nums) {
        int ans = INT_MAX;
        for( int x : nums){
            int s = 0;
            while( x > 0){
                int a = x % 10;
                s+=a;
                x = x / 10;
            }
            ans = min(ans, s);
        }
        return ans;
    }
};