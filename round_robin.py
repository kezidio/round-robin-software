
"""
Author: Kaweny Ezidio

Date: 10/30/2022

Description:  This program makes a round-robin schedule, it has a function that
takes one parameter (list of names) and returns a value in a tuple that contains
all possible pairs of names without duplicates.


"""
#idle

#create a function that takes one parameter(list of names)
def generate_round_robin_schedule(name_list):
  #declare all variables and make a copy of the original list
  list_copy = list(name_list)
  firs_elem_list = []
  pairs = []

#add an extra element to the list (bye) when the list has an odd total of elements.
  if (len(list_copy) % 2 != 0):
    list_copy.append('bye')
  
#find the first element of the list 
  first_element = list_copy[0]
  
#store the first element in a new list
  firs_elem_list.append(first_element)
  #create a variable to store the last element for shifting
  last_element = ''
  
#create a loop to access each item of the list for shifting
  for item in range(len(list_copy)-1):
    #create an inner loop to access the list half way for shifting
      for i in range((len(list_copy) // 2)):
        #define pair order in a variable called my_tuple
        #(first item, last item)
          my_tuple = (list_copy[i],list_copy[-1-i])
          #add pair to the list
          pairs.append(my_tuple)
#take the last element out of the list copy and store it in the variable last_element   
      last_element = list_copy.pop(-1)
#add the last element of the list copy to index 0
      list_copy[0] = last_element
#concatenate the first item stored in a separate list and the rest of the list
      #that is shifting
      list_copy = firs_elem_list + list_copy
      
#return the tuple      
  return pairs

#create the main function 
def main():

    # ask user for input (comma-separated values)
    user_input = input("Enter the names separated by commas (e.g. A,B,C,D,E): ")

    # convert input string into a list
    items = [item.strip() for item in user_input.split(",")]

    # generate pairs
    all_pairs = generate_round_robin_schedule(items)

    # print result
    print(all_pairs)
    
#call the main function
main()   
    







