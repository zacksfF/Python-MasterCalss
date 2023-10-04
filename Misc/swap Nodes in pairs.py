class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        else: 
            dummy = ListNode(0)
            dummy.next = head
            fast = dummy
            slow = dummy
            for i in range(n):
                fast = fast.next
            
            while fast.next != None:
                fast = fast.next 
                slow = slow.next
            
            slow.next = slow.next.next

            return dummy.next