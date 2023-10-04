class Solution(object):
    def deleteDuplicates(self, head):
        if head  == None:
            return head
        elif head != None and head.next == None:
            return head
        else:
            lookup = {}
            current = head
            prev = head
            while current != None:
                if current.val in lookup:
                    prev.next = prev.next.next
                else:
                    lookup[current.val] = True
                    prev = current
                current = current.next
            return head
