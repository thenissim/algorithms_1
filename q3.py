# ~~~ This is a template for question 3  ~~~

#Imports:

#Path for data:
path='Write here the file path, and use is later'

#Implement HashTable class:
class HashTable:
    def __init__(self, size=int , hash_function_method=str, collision_handling=str,m=int,A=float,m_2=None,A_2=None): #Initiate all the parameter for the hash table.
        if not isinstance(size, (int)):  # check if  size is an int
            raise ValueError('size should be an int')
        if not isinstance((hash_function_method), (str)):  # check if  hash_function_method is an str
            raise ValueError('hash_function_method should be an str')
        if not isinstance((collision_handling), (str)):  # check if  collision_handling is an str
            raise ValueError('collision_handling should be an str')

        if not isinstance(m, (int)):  # check if  m is an int
            raise ValueError('m should be an int')
        if not isinstance(A, (float,int)):  # check if  A is an float
            raise ValueError('A should be an float')

        if m_2 is not None:
            if not isinstance(m_2, (int)):  # check if  m_2 is an int
                raise ValueError('m_2 should be an int')

        if A_2 is not None:
            if not isinstance(A_2, (float, int)):  # check if  A_2 is an float
                raise ValueError('A_2 should be an float')

        self.hash_function_method=hash_function_method
        self.collision_handling=collision_handling
        self.size = size
        self.keys =[[] for _ in range(size)] #Data structure for keys.
        self.data = [[] for _ in range(size)]#Data structure for values.
        self.m=m
        self.A=A
        self.m_2=m_2
        self.A_2=A_2
        self.num_keys=0
        #Check that all the parameters are given for a specific configuration of the hash table:
        if self.hash_function_method=="multiplication" and self.A ==float:
            raise ValueError('Need to define A')
        if self.collision_handling=="OA_Double_Hashing" and self.m_2 ==int:
            raise ValueError('Need to define m_2')
        if self.collision_handling=="OA_Double_Hashing" and self.hash_function_method=="multiplication" and self.A_2 ==float:
            raise ValueError('Need to define A_2')

###Part A###

    def hash_function(self,key):                #Logic of hash function.
        if self.hash_function_method=="mod":
            return (self.m-key%self.m)
        elif self.hash_function_method=="multiplication":
            return int(self.m*(key*self.A-int(key*self.A)))

    def hash_function_2(self,key):              #Logic of hash function, when using OA_Double_Hashing.
        if self.hash_function_method=="mod":
            return (self.m_2-key%self.m_2)
        elif self.hash_function_method=="multiplication":
            return int(self.m_2*(key*self.A_2-int(key*self.A_2)))


    def insert(self,key=int,value=str):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')
        if not isinstance(value, (str)):  # check if  str is an int
            raise ValueError('value should be an str')

        counter=0                           #We will use the counter later to create our metric of efficiency.
        place= self.hash_function(key)
        if self.keys[place]==[] or self.keys[place]==[-1] :            #If we did not have any collision.
            self.keys[place]=[key]
            self.data[place]=[value]
            counter+=1
            self.num_keys += 1
            return counter
        elif self.keys[place]==[key]:       #Replacing the value.
            self.data[place]=[value]
            counter+=1
            return counter
        #hendeling collisions:
        elif self.collision_handling=="Chain":
            counter+=1
            for i in range(1,len(self.keys[place])):
                counter+=1
                if self.keys[place][i]==key:        #Replacing the value.
                    self.data[place][i]=value
                    self.num_keys += 1
                    return counter                  #Returns the amount of operations.
            self.keys[place].append(key)            #Using 'Chain'.
            self.data[place].append(value)
            self.num_keys += 1
            return counter                          #Returns the amount of operations.

        elif self.collision_handling=="OA_Quadratic_Probing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1

###Part B###
                new_place= self.hash_function(place + i**2)

                if self.keys[new_place]==[key]:         #Replacing the value.
                    self.data[new_place]=[value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[] or self.keys[new_place]==[-1]:
                    self.keys[new_place]=[key]          #Using 'OA_Quadratic_Probing'.
                    self.data[new_place]=[value]
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

        elif self.collision_handling=="OA_Double_Hashing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=(self.hash_function(key)+i*self.hash_function_2(key))%self.m
                if self.keys[new_place] == [key]:       #Replacing the value.
                    self.data[new_place] = [value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[] or self.keys[new_place]==[-1]:
                    self.keys[new_place]=[key]
                    self.data[new_place]=[value]        #Using 'OA_Double_Hashing'.
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

    def delete(self,key=int):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')

        counter = 0                                     #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:
            self.keys[place]==[-1]
            del self.data[place]
            counter += 1                                #If we did not have any collision.
            self.num_keys -= 1                          #Update the number of keys in the hash table.
            return counter                              #Returns the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return "Data is not in Hash Table",counter  #Data is not in Hash Table, Returns the amount of operations.
            counter+=1
            for i in range(1,len(self.keys[place])):
                counter += 1
                if self.keys[place][i] == key:
                    del self.keys[i]                   #Go over all keys in a specific place in the hash table.
                    del self.data[place][i]
                    self.num_keys -= 1                 #Update the number of keys in the hash table.
                    return counter                     #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table",counter #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(place + i * i)
                if self.keys[new_place] == []:              #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    self.keys[new_place]=-1
                    del self.data[new_place]                #Go over all places the key can be - using OA Quadratic Probing.
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table",counter      #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):
                counter += 1

###Part C###
                new_place = (self.hash_function(key)+i*self.hash_function_2(key))%self.m

                if self.keys[new_place] == []:              #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    self.keys[new_place]=-1                #Go over all places the key can be - using OA Double Hashing.
                    del self.data[new_place]
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table"  ,counter    #Data is not in Hash Table, Returns the amount of operations.

    def member(self, key=int):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')

        counter = 0                                         #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:                       #If we did not have any collision.
            counter += 1
            return True, counter                            #Returns True and the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == [] or self.keys[place] == [-1] :
                counter += 1
                return False, counter                       #Go over all keys in a specific place in the hash table,
                                                            #if the key is in it return True and the amount of operations,
            counter+=1                                      #elsr False and the amount of operations
            for i in range(1,len(self.keys[place])):
                counter += 1
                if self.keys[place][i] == key:
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):

                counter += 1                                    #Go over all places the key can be - using OA Quadratic Probing,
                new_place = self.hash_function(place + i * i)   #if the key is in it return True and the amount of operations,
                if self.keys[new_place] == []:                  #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:               #else False and the amount of operations.
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):                                                          #Go over all places the key can be - using OA Double Hashing,
                counter += 1                                                                       #if the key is in it return True and the amount of operations,
                new_place = (self.hash_function(key) + i * self.hash_function_2(key)) % self.m     #else False and the amount of operations.
                if self.keys[new_place] == []:                                                     #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    return True,counter
            return False,counter
import pandas as pd
def data_hashing(path):
    ###Part D###
    #data handling
    try:
        d1 = pd.read_excel(path, sheet_name= "Sheet1") #open each sheet in excel file
        d2 = pd.read_excel(path, sheet_name= "Sheet2")
        d3 = pd.read_excel(path, sheet_name= "Sheet3")
        l1_keys = d1["ID"].values.tolist() #convert each data frame to list
        l1_values = d1["Name"].values.tolist()
        l2_keys = d2["ID"].values.tolist() 
        l2_values = d2["Name"].values.tolist()
        l3_keys = d3["ID"].values.tolist() 
        l3_values = d3["Name"].values.tolist()
        sheet_list = [(l1_keys,l1_values),(l2_keys,l2_values),(l3_keys,l3_values)]
        size = 150
        counter_list = [] #this list will have all the dou's counters (sheet1+dou1,sheet2+dou1,sheet3+dou1,sheet1+dou2 etc..)
        
        mod_chain = [] #list that saves all hash tables with method mod, collision chain
        for sheet in sheet_list:
            counter = 0
            hash1 = HashTable (size,'mod','Chain',149,0)
            for i in range(len(sheet[0])):
                counter += hash1.insert(sheet[0][i],sheet[1][i]) 
            mod_chain.append(hash1) #list containing 3 hash tables per each sheet using mod,chain
            counter_list.append(counter)
            
        mod_quadratic = []
        for sheet in sheet_list:
            counter = 0
            hash2 = HashTable (size,'mod','OA_Quadratic_Probing',149,0)
            for i in range(len(sheet[0])):
                counter += hash2.insert(sheet[0][i],sheet[1][i])
            mod_quadratic.append(hash2) #list containing 3 hash tables per each sheet using mod,quadratic
            counter_list.append(counter)
            
        mod_dh = []
        for sheet in sheet_list:
            counter = 0
            hash3 = HashTable (size,'mod','OA_Double_Hashing',149,0,97)
            for i in range(len(sheet[0])):
                counter += hash3.insert(sheet[0][i],sheet[1][i])
            mod_dh.append(hash3) #list containing 3 hash tables per each sheet using mod,double hashing
            counter_list.append(counter)
            
        multiplication_chain = []
        for sheet in sheet_list:
            counter = 0
            hash4 = HashTable (size,'multiplication','Chain',149,0.589)
            for i in range(len(sheet[0])):
                counter += hash4.insert(sheet[0][i],sheet[1][i])
            multiplication_chain.append(hash4) #list containing 3 hash tables per each sheet using multiplication,mod
            counter_list.append(counter)
            
        multiplication_quadratic = []
        for sheet in sheet_list:
            counter = 0
            hash5 = HashTable (size,'multiplication','OA_Quadratic_Probing',149,0.589)
            for i in range(len(sheet[0])):
                counter += hash5.insert(sheet[0][i],sheet[1][i])
            multiplication_quadratic.append(hash5) #list containing 3 hash tables per each sheet using multiplication,quadratic
            counter_list.append(counter)
            
        multiplication_dh = []
        for sheet in sheet_list:
            counter = 0
            hash6 = HashTable (size,'multiplication','OA_Double_Hashing',149,0.589,97,0.405)
            for i in range(len(sheet[0])):
                counter += hash6.insert(sheet[0][i],sheet[1][i])
            multiplication_dh.append(hash6) #list containing 3 hash tables per each sheet using multiplication,quadratic
            counter_list.append(counter) 
        ###Part E###
        #efficiency value
        efficiency_value = [] #this list will have all the efficiency values
        for counter in counter_list:
            efficiency_value.append(counter/119) #always same number of elements
        
    except IOError:
        print ("can not open file")
        