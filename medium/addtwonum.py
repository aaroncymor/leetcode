class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def addTwoNumbers(l1, l2):

    print('')
    print('inside function...')

    # Declare pointers for traversal. Added for
    # clarity.

    p1 = l1
    p2 = l2

    # Declare current carry over.
    currCarry = 0

    # Declare cur variable to help traverse and
    # add nodes to new list.
    # Declare head variable to be the head of the
    # list.

    head = curr = ListNode()

    
    # Iteration condition.
    while p1 or p2 or currCarry:
        
        print(p1.val, p2.val, currCarry)

        x = l1.val + l2.val
        
        # Determine current value of carry over.
        currVal = currCarry
        currVal += 0 if p1 is None else p1.val
        currVal += 0 if p2 is None else p2.val

        if currVal >= 10:
            currVal -= 10
            currCarry = 1
        else:
            currCarry = 0

        print(currVal, currCarry)

        # Add current value as it will always
        # atleast be '1'
        curr.next = ListNode(currVal)
        curr = curr.next

        # Add base cases for iterating linked lists
        if p1 is None and p2 is None:
            break
        elif p1 is None:
            p2 = p2.next
        elif p2 is None:
            p1 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next
    
    print('exiting...')
    print('')

    # Return next node.
    return head.next


def linked_list_str(l):
    if l is None:
        return ''
    
    return str(l.val) + '->' linked_list_str(l.next)

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    