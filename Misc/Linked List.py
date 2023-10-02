class Solutions(object):
     def	detectCycle(self,	head):
           if	head	==	None:
               return	head
           else: 
                fast = head
                slow = head

                has_cycle = False
                while fast != None and fast.next != None:
                     slow = slow.next
                     fast = fast.next.next
                     if fast == slow:
                          has_cycle = True
                          break
                     if has_cycle == False:
                          return None

                     slow = head
                     while fast != slow:
                          fast = fast.next
                          slow = slow.next
                        
                     return slow