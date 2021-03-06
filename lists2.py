list1 = range(2, 20, 2)

#Find length of list1
list1_len = len(list1)
print(list1_len)

#Change the list range so it skips 3 instead of 2 numbers

list1 = range(2, 20, 3)

#Find length of list1
list1_len = len(list1)
print(list1_len)
print()

#------------------------------------------------------

#indexes
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(len(employees))
#print(employees[8]) --------------- Makes an error coz out of range
print(employees[4])
print()

#------------------------------------------------------

#Last element selection
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5)
print(last_element)
print()

#------------------------------------------------------

#Slicing lists
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
#print firt 4 items
beginning = suitcase[0:4]
print(beginning)

#select middle 2 items
middle = suitcase[2:4]

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
#Select first 3 items
start = suitcase[:3]
#Select last 2 items
end = suitcase[-2:]
print()

#------------------------------------------------------

#Counting elements in a list

#Mrs. Wilson's class is voting for class president. She has saved each student's vote into the list votes.
#Use count to determine how many students voted for 'Jake'. Save your answer as jake_votes.
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)
print()

#------------------------------------------------------

#Sorting elements in a list
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
#The print doesnt work because the sort does not return a sorted list to a variable
sorted_cities = cities.sort()
print(sorted_cities)
print()

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
#Use sorted to order games and create a new list called games_sorted
games_sorted = sorted(games)
#Use print to inspect games and games_sorted
print(games)
print(games_sorted)

#------------------------------
#All together

