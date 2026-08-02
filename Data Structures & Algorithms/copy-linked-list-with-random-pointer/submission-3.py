"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = {None: None}

        cur = head
        while cur:
            if cur not in new:
                new[cur] = Node(cur.val)

            if cur.next and cur.next not in new:
                new[cur.next] = Node(cur.next.val)
            new[cur].next = new[cur.next]

            if cur.random and cur.random not in new:
                new[cur.random] = Node(cur.random.val)
            new[cur].random = new[cur.random]
            
            cur = cur.next
        return new[head]