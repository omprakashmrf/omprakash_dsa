# front, rare, FIFO
# basic concept of queue 


class Node:
    
    def __init__(self, vale) -> None:
        self.data = vale
        self.next = None
        

class Queue:
    
    def __init__(self) -> None:
        self.front =None
        self.rare = None
        
    
    def enqueu(self, value):
        new_node = Node(value)
        if self.rare==None:
            self.front =new_node
            self.rare = self.front
        else:
            self.rare.next = new_node
            self.rare = new_node
            
    def dequeue(self):
        if self.front==None:
            return print("Empty queue")
        
        else:
            self.front = self.front.next
            
    
    def traverse(self):
        temp = self.front
        
        while temp !=None:
            print(temp.data, end=" ")
            temp = temp.next                

    def is_empty(self):
        return self.front ==None
    
    
    def size(self):
        temp = self.front
        count = 0
        
        while temp !=None:
            temp.data
            count +1
            temp = temp.next 
        
        return count                 


q = Queue()

q.enqueu(4)
q.enqueu(8)
q.enqueu(9)

q.traverse()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
#print("after delete the element")
q.traverse()

# with the help of two stacks we can perform Queue operation like (enqueue and dequeue)


              
                       
