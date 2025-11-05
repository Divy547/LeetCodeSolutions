// Last updated: 11/5/2025, 11:56:14 AM
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
    ListNode* middleNode(ListNode* head) {
        ListNode *a = head;
        ListNode *b = head;
        while(a != nullptr && a->next != nullptr){
            a = a->next->next;
            b = b->next;
        }
        return b;
    }
};