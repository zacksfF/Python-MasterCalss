class Solution(object):
    def reverseList(self, head):

        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            temp = None
            next_node = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node
            
            return temp