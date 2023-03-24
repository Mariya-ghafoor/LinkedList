# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = ListNode()

    def add_list(self, val):
        new_node = ListNode(val)

        if self.head:
            cur = self.head

            while cur.next != None:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node


    def print_list(self):
        elem = []
        cur = self.head

        elem.append(cur.val)
        while cur.next != None:
            cur = cur.next
            elem.append(cur.val)

        print(elem)

    def create_cycle(self,pos):

        cur =  self.head
        if pos == -1:
            return None
        #Tasking the cursor to last node
        while cur.next is not None:
            # print('cur.next is ',cur.next.val)
            cur = cur.next
        last_node = cur

        #Finding node where last node will be connected, starting from head
        cycle_node = self.head

        #Iterating till we reach node at position 'pos'
        for i in range(pos):
            cycle_node = cycle_node.next

        #connecting last node with the cycle node at position 'pos'
        last_node.next = cycle_node
#.................................................

    def find_cycle(self):
        node = self.head
        MySet = set()
        #Iterating through the linked list
        while node != None:
            #checking if node already exists in Myset. If yes then we have found the node where last node connects to form cycle.
            if node in MySet:
                return node
            #if node is not in MySet then add it and move on to the next node
            MySet.add(node)
            node = node.next
        return




#Creating a sample liked list [3,2,0,4]
l1 = LinkedList()
node = ListNode(1)
l1.head = node
l1.add_list(2)
l1.add_list(7)
l1.add_list(-4)
l1.add_list(19)
l1.add_list(6)
l1.add_list(-9)
l1.add_list(-5)
l1.add_list(-5)
l1.add_list(-5)
l1.print_list()

#Connecting last node of the list with node at pos = 6
l1.create_cycle(6)

print(l1.find_cycle().val) #printing node value to check if its the right node
