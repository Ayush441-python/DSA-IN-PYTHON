class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
a = Node(6)
b = Node(5)
c = Node(8)

a.next=b
b.next=c 

head = a 

print(head.data)
print(head.next.data)

## Traverse
def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" ")
        curr = curr.next

PrintLinkedList(head)

print("\n")

## Insert
### At begining 
newNode = Node(4)
newNode.next = head
head = newNode
PrintLinkedList(head)

print("\n")

### At ending
newNode = Node(1)
curr = head
while curr != None:
    newNode.next = head
    curr = curr.next



PrintLinkedList(head)

