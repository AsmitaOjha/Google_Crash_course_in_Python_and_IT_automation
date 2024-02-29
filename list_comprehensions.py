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

#skills
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years =[year.replace("2023",'2024') if year[-4:]=="2023" else year for year in years]
print(updated_years)

#skill group 4
# company = 'Sharing a bond'
def change_str(company):
	new_string = ''
	
	list_of_company=company.split(d)
	
	for x in list_of_company:
		new_string += x[1:]+'-'+ x[0]+ ' '
	return(new_string)
print(change_str("Hello I am Asmita Ojha"))