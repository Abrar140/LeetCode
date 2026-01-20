class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                # Remove duplicate node
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

def print_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Example: Creating linked list: 1 -> 2 -> 2 -> 3 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)

print("Original list:")
print_list(head)

head = remove_duplicates(head)

print("After removing duplicates:")
print_list(head)
