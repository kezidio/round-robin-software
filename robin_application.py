#idel and replit.com


def generate_round_robin_schedule(name_list):
  list_copy = list(name_list)
  # pairs = []
  firs_elem_list = []

  #adding bye if list has odd total
  if (len(list_copy) % 2 != 0):
    list_copy.append(['bye'])
  
   # storing first element in a new list
   
  char = list_copy[0]
  firs_elem_list.append(char)
  
  for i in range(len(list_copy)-1):
    
    last_element = list_copy.pop(-1)
    
    list_copy = firs_elem_list + list_copy
    
    
    
    print(list_copy)
generate_round_robin_schedule(['a', 'b', 'c', 'd','e','f','g'])



# [('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E'), ('A', 'G'), ('H', 'F'), ('B', 'E'),
# ('C', 'D'), ('A', 'F'), ('G', 'E'), ('H', 'D'), ('B', 'C'), ('A', 'E'), ('F', 'D'),
# ('G', 'C'), ('H', 'B'), ('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'H'), ('A', 'C'),
# ('D', 'B'), ('E', 'H'), ('F', 'G'), ('A', 'B'), ('C', 'H'), ('D', 'G'), ('E', 'F')]
