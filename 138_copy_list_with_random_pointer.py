from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current_node = head

        hash_map = {}

        while current_node:
            hash_map[current_node] = Node(current_node.val)
            current_node = current_node.next

        current_node = head

        while current_node:
            try:
                hash_map[current_node].next = hash_map[current_node.next]
            except KeyError:
                pass
            try:
                hash_map[current_node].random = hash_map[current_node.random]
            except KeyError:
                pass
            current_node = current_node.next

        return hash_map[head]
