#Define the function to accept one parameter for our list of numbers
#Add the last and second to last elements from our list together
#Append the calculated value to the end of our list.
#Repeat steps 2 and 3 two more times
#Return the modified list

#Write your function here
def append_sum(lst):
  lst.append(lst[-2] + lst[-1])
  lst.append(lst[-2] + lst[-1])
  lst.append(lst[-2] + lst[-1])
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
