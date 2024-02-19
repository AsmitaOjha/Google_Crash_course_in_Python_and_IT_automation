def odd_numbers(n):
	return [x for x in range(1,n+1) if x%2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(90))

couple_things=['holding hands','chocolates','hugs','intimacy','caring','love','argument','patchup','kiss','helping']
update_couple_things=[]
for we in couple_things:
	new=we.replace('helping','mood swings')
	update_couple_things.append(new)
	if we.endswith('chup'):
		new_couple_things=we.replace('chup','ch up😍')
		update_couple_things.append(new_couple_things)
									 
								 
print(couple_things)
print(update_couple_things)

def cubes(start,end):
	cubes=[x**3 for x in range(start,end+1)]
	return(cubes)
print(cubes(3,9))