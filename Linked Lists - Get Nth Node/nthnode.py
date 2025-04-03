from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index")
    current = node
    for i in range(index):
        if current.next is None:
            raise Exception("Index out of range")
        current = current.next
    return current
    
