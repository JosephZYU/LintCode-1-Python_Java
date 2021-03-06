# Given a list, rotate the list to the right by k places, where k is non-negative

# Input: 1, 2, 3, 4, 5; k=2
# Output: 4, 5, 1, 2, 3

"""
if head is None:
    return None

elif len(list) = 1:
    return list  # 单身狗列表， 只有一个值

elif k = 0:
    return break  # DO NOTHING!

elif 0 < k < len(list):
    return func(k)

else:
    k = k % len(list)
    return func(k)
"""

# 🧑‍💻 0:20:38" Line: 4 - 7

# 🧑‍💻 2:09:30"

# Starts at line 15


class listNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the list
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def get_length(self, head):
        length = 0
        while head:
            length += 1
        return length

    def rotateRight(self, head, k):
        # 👀 True, False, None -> Capitalize the 1st letter!
        if head is None:
            return None

        dummy = listNode(0)
        dummy.next = head

        length = self.get_length(head)
        k %= length
        # k = k % length # 👀 no matter how many cycles of total length, ONLY remainder matters

        # ahead
        ahead = dummy
        for _ in range(k):  # 👀 k = 2 -> 0, 1 -> perform twice!
            ahead = ahead.next

        # behind
        behind = dummy
        while ahead.next:
            behind = behind.next
            ahead = ahead.next

        # Rotate!
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None

        return dummy.next
