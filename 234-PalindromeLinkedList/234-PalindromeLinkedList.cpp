// Last updated: 10/14/2025, 12:49:30 PM
class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;

        // Find middle
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse second half
        ListNode* secondHalf = reverse(slow->next);

        // Compare first and second half
        ListNode* p1 = head;
        ListNode* p2 = secondHalf;
        bool palindrome = true;
        while (p2) {
            if (p1->val != p2->val) {
                palindrome = false;
                break;
            }
            p1 = p1->next;
            p2 = p2->next;
        }

        // Restore the list (optional)
        slow->next = reverse(secondHalf);

        return palindrome;
    }
};
