def loop_size(node):
    if node is None:
        return 0
    slow = node
    fast = node.next
    while slow != fast:
        if fast is None or fast.next is None:
            return 0
        slow = slow.next
        fast = fast.next.next
    count = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        count += 1
    return count