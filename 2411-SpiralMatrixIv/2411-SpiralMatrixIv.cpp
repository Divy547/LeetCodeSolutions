// Last updated: 3/22/2026, 10:33:15 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> matrix(m, vector<int>(n, -1));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                matrix[i][j] = -1;
            }
        }
        for(vector<int> x : matrix){
            for(int y : x){
                cout<<y<<" ";
            }
        }
        int top = 0;
        int left = 0;
        int bottom = m - 1;
        int right = n - 1;
        while(top <= bottom && left <= right && head){
            for (int j = left; j <= right && head; ++j) {
                matrix[top][j] = head->val;
                head = head->next;
            }
            top++;
            for(int i = top; i <= bottom && head; ++i){
                matrix[i][right] = head->val;
                head = head->next;
            }
            right--;
            if(top <= bottom){
                for(int j = right; j >= left && head; --j){
                    matrix[bottom][j] = head->val;
                    head = head->next;
                }
                bottom--;
            }
            if(left <= right){
                for(int i = bottom; i >= top && head; --i){
                    matrix[i][left] = head->val;
                    head = head->next;
                }
                left++;
            }
        } 
        return matrix;  
    }    
};