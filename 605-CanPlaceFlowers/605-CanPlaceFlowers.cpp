// Last updated: 3/22/2026, 10:34:00 PM
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0;
        int j = 1;
        int k = 0;
        int cnt = 0;
        while(i < flowerbed.size() && n > 0){
            j = (i == 0) ? 0 : flowerbed[i-1];
            k = (i == flowerbed.size() - 1) ? 0 : flowerbed[i+1];
            
            if(flowerbed[i] == 0 && j == 0 && k == 0){
                i+=2;
                cnt++;
            }else{
                i++;
            }
        }
        return cnt >= n;
    }
};