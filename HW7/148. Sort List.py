Given the head of a linked list, return the list after sorting it in ascending order.

Eample 1:
  - Input: head = [4,2,1,3]
  - Output: [1,2,3,4]

Example 2:
  - Input: head = [-1,5,3,4,0]
  - Output: [-1,0,3,4,5]

Example 3:
  - Input: head = []
  - Output: []

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

=================================================================================

# method 1 : linked list -> array，array -> linked list

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def convert_to_listnode(l, head=None, current=None, index=0):
            if(index > len(l)-1):
                return head

            if(head == None):
                head = ListNode(l[index])
                current = head
                return convert_to_listnode(l, head, current, index+1)

            next_node = ListNode(l[index])
            current.next = next_node
            current = next_node
            index += 1
            return convert_to_listnode(l, head, current, index)
        
        
        if not head or not head.next:
            return head
        
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        dummy = convert_to_listnode(arr)
        
        return dummy
    
=================================================================================

# method 2 : merge

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # split the list into two halfs
        left = head
        right = self.getMid(head)  # 找到linked list的中間點
        tmp = right.next
        right.next = None  # 左堆建立完成
        right = tmp  # 右堆建立完成
        
        # recursive to merge the result
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        if h1:
            tail.next = h1
        if h2:
            tail.next = h2
            
        return dummy.next
