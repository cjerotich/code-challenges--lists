#Define the function to accept one parameter for our list
#Get the length of the list
#Append the length of the list to the end of the list
#Return the modified list

#Write your function here
def append_size(lst):
  length = len(lst)
  lst.append(length)
  return lst
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
