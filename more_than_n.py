#Define the function to accept three parameters, a list of numbers,
#a number to look for, and a number for the number of instances
#Count the number of occurrences of item (the second parameter)
#in lst (the first parameter)
#If the number of occurrences is greater than n (the third parameter),
#return True. Otherwise, return False

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
