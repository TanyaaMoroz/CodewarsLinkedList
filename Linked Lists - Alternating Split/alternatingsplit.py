class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise Exception("List must contains two nodes.")

    first = head
    second = head.next 
    first_tail, second_tail = first, second  
    current = second.next  

    while current:
        first_tail.next, first_tail = current, current  
        current = current.next  
        if current:
            second_tail.next, second_tail = current, current  
            current = current.next  

    first_tail.next = second_tail.next = None  
    return Context(first, second)