class Node:
    def __init__(self,datavalue = None):
        self.datavalue = datavalue
        self.next = None

class Linkedlist:
    def __init__(self):
        self.headvalue = None

    # Traversing
    def print(self):
        printvalue = self.headvalue
        while printvalue != None:
            print(printvalue.datavalue)
            printvalue = printvalue.next

    # Insertion at begining
    def insertatbegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.headvalue
        self.headvalue = NewNode

    # Insertion at the end
    def insertatend(self,newdata):
        NewNode = Node(newdata)
        if self.headvalue == None:
            self.headvalue = NewNode
            return

        end = self.headvalue
        while end.next != None:
            end = end.next
        end.next = NewNode

    #insertion at the mid
    def insertatmid(self,prev_node,newdata):
        NewNode = Node(newdata)
        if prev_node == None:
            print("The prev_node must be in the linkedlist")
            return
        NewNode.next = prev_node.next
        prev_node.next = NewNode

    #deletion or removal of a node
    def deletnode(self,key):
        temp = self.headvalue
        if (temp is not None):
            if temp.datavalue == key:
                self.headvalue = temp.next
                temp = None
                return
        while temp is not None:
            if temp.datavalue == key:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next
            temp = None



new_list = Linkedlist()
new_list.headvalue = Node(1)
e2 = Node(2)
e3 = Node(3)

new_list.headvalue.next = e2
e2.next = e3

# new_list.insertatbegining(9)
# new_list.insertatend(13)
# new_list.insertatmid(e2,5)
new_list.deletnode(new_list.headvalue.next)
new_list.print()





