class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def parse(string):
    if string.lower() in ("null", "none"):
        return None
    
    nodes = string.split(" -> ") 
    
    if nodes[-1].lower() in ("null", "none"):
        nodes.pop()

    head = Node(int(nodes[0]))
    current = head
    
    for value in map(int, nodes[1:]):
        current.next = Node(value)
        current = current.next
    
    return head

def linked_list_from_string(s):
    return parse(s)