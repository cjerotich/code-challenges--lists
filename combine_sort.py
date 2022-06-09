#Define the function to accept two parameters, one for each list.
#Combine the two lists together
#Sort the result
#Return the sorted and combined list



#Write your function here
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList =  sorted(unsorted)
  return sortedList
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

