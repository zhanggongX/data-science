# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head.next
        slow = head

        while fast:
            if fast.val == 0:
                if fast.next is None:
                    slow.next = None
                    break

                slow.next = fast
                slow = slow.next
                fast = fast.next
                continue

            slow.val += fast.val
            fast = fast.next

        return head


if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(0, ListNode(2, ListNode(3, ListNode(0, ListNode(4, ListNode(0))))))))
    res = Solution().mergeNodes(head)
    while res:
        print(res.val)
        res = res.next
