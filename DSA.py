# Linked List


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(Node):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def reverse_list(self):
        current = self.head
        prev = None
        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if (l1 or l2) is None:
            return l1 or l2

        dummy = Node(data)
        dummy_head = dummy
        rem = carry = 0
        while l1 is not l2:
            sum = l1.val + l2.val
            if sum > 9:
                rem = sum % 10
                d1 = ListNode(rem+carry)
                dummy.next = d1
                carry = 1
            else:
                d1 = ListNode(sum+carry)
                dummy.next = d1
                carry = 0
            dummy = dummy.next
            l1 = l1.next if l1.next else dummy_head
            l2 = l2.next if l2.next else dummy_head
        return dummy_head.next


link = LinkedList()
link1 = LinkedList()
# link.head = Node(1)
# link.head.next = Node(2)
# link.head.next.next = Node(3)


link.append(9)
link.append(9)
link.append(9)
link.append(9)
link.append(9)
link.append(9)
link.append(9)
link1.append(9)
link1.append(9)
link1.append(9)
link1.append(9)
# link.print_list()
# link.push(1)
# link.print_list()
# print('Reversed')
# link.reverse_list()
link1.print_list()
print(link.addTwoNumbers(link, link1))
# rev.print_list()
