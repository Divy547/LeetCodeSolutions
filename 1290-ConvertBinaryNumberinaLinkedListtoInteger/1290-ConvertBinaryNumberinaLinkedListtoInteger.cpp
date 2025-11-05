// Last updated: 11/5/2025, 1:48:25 PM
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
    int getDecimalValue(ListNode* head) {
        int num = 0;
        int count = 0;
        ListNode *temp = head;
        while(temp != nullptr){
            count++;
            temp = temp->next;
        }
         ListNode *temp2 = head;
        for (int i = count - 1; i >= 0 ; i--){
            num += (temp2->val)*pow(2,i);
            temp2 = temp2->next; 
        }
        return num;
    }
};