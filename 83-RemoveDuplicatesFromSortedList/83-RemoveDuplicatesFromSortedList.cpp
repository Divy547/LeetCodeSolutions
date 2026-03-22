// Last updated: 3/22/2026, 10:34:44 PM
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