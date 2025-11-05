// Last updated: 11/5/2025, 12:53:57 PM
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *temp = head;
        while(temp != nullptr && temp->next != nullptr){
           if(temp->next->val == temp->val){
                temp->next = temp->next->next;
           }else{
                temp = temp->next;
           }
        }
        return head;
    }
};