# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses = [2200, 2350, 2600, 2130, 2190]
print(f"Amout spend extra in Feb compare to January: {expenses[1]-expenses[0]}")
print(f"Total expense in first quarter of the year is: {expenses[0]+expenses[1]+expenses[2]}")
for x in expenses:
    if x==2000:
        print(f"in {x+1}th month I spent exactly 2000 dollars")
    else:
        print("I donot spend exacly 2000 in any month")
expenses.append(1980)
print(expenses)
expenses[3]=expenses[3]-200
print(expenses)

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
index_hulk=heros.index('hulk')
heros.insert(index_hulk + 1, 'black panther')  # Add 'black panther' after 'hulk'
print("List after adding 'black panther' after 'hulk':", heros)

print(dir(list))
# heros.sort()
# print(heros)
new_sorted=sorted(heros)
print(heros)
print(new_sorted)

