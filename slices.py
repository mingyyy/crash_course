'''
4-10.
Slices: Using one of the programs you wrote in this chapter,
        add several lines to the end of the program that do the following:
• Print the message, The first three items in the list are: .
  Then use a slice to print the first three items from that program’s list .
• Print the message, Three items from the middle of the list are: .
  Use a slice to print three items from the middle of the list .
• Print the message, The last three items in the list are: .
  Use a slice to print the last three items in the list .
'''

trip =['Barcelona','iceland','alaska','boswana','congo', 'morroco', 'columbia','brazil','south africa']
print(trip[:3])

if len(trip)%2 ==0: # if there is an even number of list, can't be in the middle, so one space less in front
    start = int(len(trip)/2 - 2)
    end = int(len(trip)/2 + 1)
else:
    start = int((len(trip)-1)/2 -1)
    end = start + 3
print(start, end)
print(trip[start:end])

print(trip[-3:])