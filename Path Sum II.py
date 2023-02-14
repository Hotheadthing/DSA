def __init__(self):
    self.headvalue = None
def traverse(self):
    printvalue = self.headvalue

    while printvalue != None:
        print(printvalue.datavalue)
        printvalue = printvalue.next