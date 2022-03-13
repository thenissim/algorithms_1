# ~~~ This is a template for question 2  ~~~

#Imports:

###Part A###
#~~~  implementation of heap class  ~~~

class Heap():
    def __init__(self, A):
        self.t = A #receiving the unorganized list which later will be organized as a heap
        if type(self.t)!=list:
            raise ValueError('A is not a list')            
        for elem in self.t: #making sure all of t's elements are numbers
            if isinstance(elem, int) or isinstance(elem, float): 
                continue 
            else:
                raise ValueError('not all elements are numbers')
        self.size = len(self.t) 
        self.build_heap() #changing the list attribute to be an arranged min heap

    def insert(self, x):
        if type(x)!=int and type(x)!=float: 
            raise ValueError('x must be a number')
        self.size = self.size +1
        self.t.append(x)
        cur = self.size
        while cur > 1 and self.t[cur-1] < self.t[cur//2-1]:# while dad is bigger than son and cur isnt the root
            self.t[cur-1],self.t[cur//2-1] = self.t[cur//2-1],self.t[cur-1]
            cur = cur//2        

    def delete_min(self):
        if self.size == 0:
            raise ValueError('heap is already empty')
        mini = self.t[0]
        if self.size == 1: #heap has only a root
            self.t.pop(0)
            self.size -= 1
            return mini 
        self.t[0],self.t[self.size-1] = self.t[self.size-1],self.t[0] #exchanging root and last leaf
        self.t.pop(self.size-1) #removing the min 
        self.size -=1
        self.heapify(0) #'lowering' the new root down the heap
        return mini
            
    def heapify(self,i):
        if (2*(i+1)-1) > self.size-1: #checking if i is a leaf
            return None
        if (2*(i+1)) > self.size-1: #checking if i has a left son
            if self.t[i] > self.t[2*i+1]: #checking if son is smaller than parent
                self.t[i],self.t[2*i+1] = self.t[2*i+1],self.t[i]
                return None
        else: #i has two sons
            if self.t[2*i+1] < self.t[2*(i+1)]: #checking which of the sons is smaller
                j = 2*i+1
            else:
                j = 2*(i+1)
            if self.t[i] > self.t[j]:
                self.t[i],self.t[j] = self.t[j],self.t[i] #exchanging parent with smaller of two sons
                self.heapify(j) #recursive call to the function
            else:
                return None
            
    def build_heap(self): 
        for i in range(self.size//2,-1,-1): 
            self.heapify(i)

###Part B###
def optimal_coin_collector(coins=list): #explained in PDF
    n = len(coins)
    heap = Heap(coins)
    cur = heap.delete_min()
    cur += heap.delete_min() #first union
    cur *= n-1
    while heap.size > 0:
        cur += heap.size * heap.delete_min()
    return cur #The time is takes to create al the merges



