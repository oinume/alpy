class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    current = 0
    prev = None
    node = head
    if head is None:
        node = Node(data)
        return node
    while node is not None:
        if position == current:
            n = Node(data, node)
            if prev is not None:
                prev.next = n
            else:
                return n
            #node.next = n
            #return head
        prev = node
        node = node.next
        current += 1
    return head

# 0: a, next=b
# 1: b, next=c
# 2: c, next=None

# 0: a, next=x # next=xにする
# 1: x, next=b # next=bにする
# 2: b, next=c
# 3: c, next=None

# head.data=2, data=3, position=0
# head.data=2, data=5, position=1
# head.data=2, data=4, position=2
# head.data=2, data=2, position=3
# head.data=2, data=10, position=1

# head.data=2, data=3, position=0
# 2
# head.data=2, data=5, position=1
# 2
# head.data=2, data=4, position=2
# 2
# head.data=2, data=2, position=3
# 2
# head.data=2, data=10, position=1
# 2


def print_node(head):
    n = head
    while n is not None:
        print(n.data)
        n = n.next


if __name__ == '__main__':
    c = Node('c', None)
    b = Node('b', c)
    a = Node('a', b)
    print_node(a)
    print("---")
    head = InsertNth(a, 'x', 0)
    print_node(head)
