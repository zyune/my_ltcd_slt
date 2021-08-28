# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    
    def aaaa():
        print("ssssss")
    def hasCycle(self, head):
        seen = set();
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return false
        def rabbitandtortoise(self, head):
            if not head or not head.next:
                return False
        #上面的操作相当于考虑一下边界情况
        #if (head == null || head.next == null) {
        #     return false;
        # }
        rabbit = head
        tortoise = head.next
        while rabbit!=tortoise:
            if not rabbit or not rabbit.next: 
                #当快指针=null 了那就不是循环链表了
                return False
            tortoise=tortoise.next
            rabbit=rabbit.next.next
        return true
a =9
b=int(a/2) 
print(b)          
            
    # h = [3,2,0,-4]      
    # head = ListNode(h.pop(0))
    # head.next = ListNode(h.pop(0))
    # ln1= head.next
    # ln1.next = ListNode(h.pop(0))
    # ln2= ln1.next
    # ln2.next = ListNode(h.pop(0))
    # ln3= ln2.next
    # ln3.next = ln1
    # print(head)
    # aaaa()
    # hasCycle(head)

    
                



