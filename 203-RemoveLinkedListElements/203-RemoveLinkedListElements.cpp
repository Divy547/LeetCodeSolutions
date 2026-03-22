// Last updated: 3/22/2026, 10:34:33 PM
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
    ListNode* removeElements(ListNode* head, int val) {
        while(head != nullptr && head->val == val) {
            head = head->next;
        }
        
        ListNode *temp = head;
        while(temp != nullptr && temp->next != nullptr){
            if(temp->next->val == val){
                if(temp->next->next != nullptr)
                    temp->next = temp->next->next;
                else
                    temp->next = nullptr;
            }else{
                temp = temp->next;
            }
            
        }
        return head;
    }
};