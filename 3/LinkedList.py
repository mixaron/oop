class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def len(self):
        walker = self.start
        count = 0
        while walker is not None:
            walker = walker.next
            count += 1
        return count
    
    def search(self, data):
        walker = self.start
        while walker is not None:
            if walker.data == data:
                return walker
            walker = walker.next
        return None
    
    def append(self, obj):
        new_node = Node(obj)
        if self.end is not None:
            self.end.next = new_node
            self.end = new_node
        else:
            self.end = new_node 
    
    def remove(self, index):
        if index < 0:
            return "Index cannot be less 0"
        
        if index == 0:
            if self.start is None:
                return "Nothing to remove"
            
            if self.start.next is not None:
                self.start = self.start.next
            else:
                self.start = None
            return
        
        walker = self.start
        previous = None
        current_index = 0

        while walker is not None and current_index < index:
            previous = walker
            walker = walker.next
            current_index += 1

        if walker is None:
            return "index out of bounds"
        
        previous.next = walker.next

        if walker == self.end:
            self.end = previous