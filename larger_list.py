#Define the function to accept
#two parameters for our two lists of numbers
#Check if the length of the first list is greater than
#or equal to the length of the second list
#If true, then return the last element from the first list.
#Otherwise, return the last element from the second list

#Write your function here
def larger_list(lst1,lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
