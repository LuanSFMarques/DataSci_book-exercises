mylist = [1,2,3,4]


mylist[len(mylist):] = [5,6]

print(mylist)


del mylist[len(mylist)-3:] # Delete the last 3 elements of the list

print(mylist)


