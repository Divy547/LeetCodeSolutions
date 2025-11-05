// Last updated: 11/5/2025, 5:34:58 PM
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
        ListNode* dummy = new ListNode(0, head);
        ListNode* temp = dummy;
        while (temp->next && temp->next->next) {
            if (temp->next->val == temp->next->next->val) {
                int dup = temp->next->val;
                // skip all nodes with val == dup
                while(temp->next && temp->next->val == dup){
                    temp->next = temp->next->next;
                }
            } else {
                temp = temp->next;
            }
        }
        return dummy->next;
    }
};