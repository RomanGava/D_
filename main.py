# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Функция для печати заданного связанного списка
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Переворачивает данный связанный список, изменяя его поля `.next` и
# 1ТП4Т его голова.
def reverse(head):
 
    previous = None
    current = head
 
    # пройтись по списку
    while current:
 
        # хитрый: обратите внимание на следующий узел
        next = current.next
 
        current.next = previous        # исправить текущий узел
 
        previous = current
        current = next
 
    # зафиксируйте головку так, чтобы она указывала на новый фронт
    return previous
 
 
if __name__ == '__main__':
 
    head = None
    for i in reversed(range(6)):
        head = Node(i + 1, head)
 
    head = reverse(head)
    printList(head)