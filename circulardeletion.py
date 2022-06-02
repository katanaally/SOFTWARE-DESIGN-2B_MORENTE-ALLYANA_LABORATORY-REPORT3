class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

def push(head_ref, data):

    ptr1 = Node()
    ptr1.data = data
    ptr1.next = head_ref

    if (head_ref != None):

        temp = head_ref
        while (temp.next != head_ref):
            temp = temp.next
        temp.next = ptr1

    else:
        ptr1.next = ptr1

    head_ref = ptr1
    return head_ref

def printList(head):
    temp = head
    if (head != None):
        while (True):
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == head):
                break
    print()

def deleteNode(head, key):
    # If linked list is empty
    if (head == None):
        return

    if ((head).data == key and (head).next == head):
        head = None

    last = head
    d = None

    if ((head).data == key):

        while (last.next != head):
            last = last.next

        last.next = (head).next
        head = last.next

    while (last.next != head and last.next.data != key):
        last = last.next

    if (last.next.data == key):
        d = last.next
        last.next = d.next

    else:
        print("no such keyfound")

    return head

head = None

head = push(head, 6)
head = push(head, 5)
head = push(head, 11)
head = push(head, 16)
head = push(head, 20)

print("List Before Deletion: ")
printList(head)

head = deleteNode(head, 6)

print("List After Deletion: ")
printList(head)


