# ~~~ This is a template for question 1  ~~~

#Imports:

###Part A###
#~~~  implementation of queue class  ~~~
class Queue(): 
    class Node():
    	def __init__(self, x, next_): #x is the node's data
            self.x = x 
            self.next_ = next_
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0
                
    def front(self):
        if self.empty():
            raise IsEmptyError('Queue is empty, can not return front')
        return self.head.x
    
    def empty(self): 
        return self.q_size == 0
    
    def enqueue(self, x): #x is the element recieved
        new = self.Node(x, None) #defining a new node so we can connect it
        if self.empty():
            self.head = new
        else:
            self.tail.next_ = new #connecting the new node to the end
        self.tail = new #new was added to the end
        self.q_size += 1
        
           
    def dequeue(self): 
        if self.empty():
            raise IsEmptyError('can not erase node from empty queue')
        result = self.head.x
        self.head = self.head.next_
        self.q_size -= 1
        if self.empty():
            self.tail = None
        return result
    
class IsEmptyError(Exception):
    pass


###Part B###
def reverse_k_first_elements(A=list,k=int):
    if type(A) != list or type(k) != int:
        raise ValueError('incorrect input')
    if len(A) <= 1: #if the list is empty or with one element, for every k the list will remain the same
        return A
    if k>len(A):
        raise ValueError('k larger than number of values in A')
    if k==0:
        return A #no need to make changes when k is 0
    q_lst = Queue()
    for val in A[:k]:
        q_lst.enqueue(val) #putting first k elements in queue
        A.remove(val) #removing them from list
    while not q_lst.empty():
        cur = q_lst.dequeue() #removing FIFO method from queue
        A.insert(0,cur) #inserting in reverse order
    return A #List with the defined order


