
class RoundRobin:
    def __init__(self, list_of_strings):
        self.names = [] + list_of_strings

        #if (len(self.names) % 2 != 0):
          #  self.names.append('bye')
            
    def generate_round(self):
        pairs = []
        last_element = ''
        firs_elem_list = []
        first_element = self.names[0]
        firs_elem_list.append(first_element)
        #start = 0
       # end = 0
       # rounds = []
        for item in range(len(self.names)-1):
            #count = []
            for i in range((len(self.names) // 2)):
                my_tuple = (self.names[i],self.names[-1-i])
                pairs.append(my_tuple)
            last_element = self.names.pop(-1)
            self.names[0] = last_element
            self.names = firs_elem_list + self.names
            my_tuple = (self.names[i],self.names[-1-i])
            
#I have all the pairs and now I need to seperate them and return a different
#interation every call
            
        print(pairs)   #to see whats going on
"""
#maintain state??

        x = len(self.names) // 2
        y = x * len(self.names)-1

        #return 
        
   1st    print(pairs[:4])   pairs[0 : x] len of list
        
   2nd     print(pairs[4:8])  pairs[x : x*2] len list + len list
        
   3rd     print(pairs[8:12]) pairs[x*2 : x*3]
        
    4th    print(pairs[12:16])pairs[x*3 : x*4]
        
    5th    print(pairs[16:20])pairs[x*4 :x*5]
        
    6th    print(pairs[20:24])pairs[x*5 :x*6]
        
    7th    print(pairs[24:28]) pairs[x*6 :x*y] 

            
"""
        #   
       # end += x
       # rounds += pairs[start:end]
       # start += x
       # end += x + x
      #  rounds += pairs[start:end]
       # print(rounds)
        
              
        #for rows in range(len(pairs)):
            
            #print(rows)
        #pairs
           
    #def get_names(self):
     #   return self.names
            
def main():
    list_of_names = RoundRobin(["A","B","C","D","E","F","G","H"])
    list_of_names.generate_round()
    
    
    
main()

"""
Create a method called generate_round. This method should only have one
parameter - self. The first time this method is called on a RoundRobin object,
the method should return the first round as a list of tuples, where each tuple
is a pair of names that should be matched for that round. Each time the method
is called after that, it should return the pairs for the next round.

Take, for example, the list of names given in the instructions for Project 8:

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
The first time, the generate_rounds method should return:

[('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E')]
The next time, it should return:

[('A', 'G'), ('H', 'F'), ('B', 'E'), ('C', 'D')]
... And so on and so forth.

It is up to you how to handle the case where the method is called too many
times. You can either continue to loop through the pairs again or print an
error.

It is also up to you how to implement this step. You can generate all the
rounds ahead of time, and then return them as they are needed. Alternatively,
you can generate each round when the method is called. Either way, you'll
probably want to have your Project 8 code on hand so you can recycle the
relevant pieces.
"""

