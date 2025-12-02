// Last updated: 12/2/2025, 10:16:01 PM
1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode() : val(0), next(nullptr) {}
7 *     ListNode(int x) : val(x), next(nullptr) {}
8 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
9 * };
10 */
11class Solution {
12public:
13    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
14        vector<vector<int>> matrix(m, vector<int>(n, -1));
15        for(int i = 0; i < m; i++){
16            for(int j = 0; j < n; j++){
17                matrix[i][j] = -1;
18            }
19        }
20        for(vector<int> x : matrix){
21            for(int y : x){
22                cout<<y<<" ";
23            }
24        }
25        int top = 0;
26        int left = 0;
27        int bottom = m - 1;
28        int right = n - 1;
29        while(top <= bottom && left <= right && head){
30            for (int j = left; j <= right && head; ++j) {
31                matrix[top][j] = head->val;
32                head = head->next;
33            }
34            top++;
35            for(int i = top; i <= bottom && head; ++i){
36                matrix[i][right] = head->val;
37                head = head->next;
38            }
39            right--;
40            if(top <= bottom){
41                for(int j = right; j >= left && head; --j){
42                    matrix[bottom][j] = head->val;
43                    head = head->next;
44                }
45                bottom--;
46            }
47            if(left <= right){
48                for(int i = bottom; i >= top && head; --i){
49                    matrix[i][left] = head->val;
50                    head = head->next;
51                }
52                left++;
53            }
54        } 
55        return matrix;  
56    }    
57};