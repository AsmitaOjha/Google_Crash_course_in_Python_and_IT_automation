# #Country	Population
# # China	143
# # India	136
# # USA	32
# # Pakistan	21
# def country_pop():
#     country_pop={'china':143,'India':136,'USA':32,'Pakistan':21}
#     print(country_pop)
#     x=input("Enter from these four options: 1.print /n 2.add/n3.remove/n4.query: ")
#     if x.lower()=='print':
#         for key,value in country_pop.items():
#             print(key,"==>",value)
#     if x.lower()=='add':
#         country_name=input("Enter country name")
#         if country_name in country_pop:
#             print("Already exists")
#         else:
#             country_population=input("Enter population : ")
#             country_pop[country_name]=country_population
#             for key,value in country_pop.items():
#                 print(key,'==>',value)
#     if x.lower()=='remove':
#         country_name=input("Enter the country you want to remove from dictionary: ")
#         if country_name in country_pop:
#             del country_pop[country_name]
#             for key,value in country_pop.items():
#                 print(key,'==>',value)
#         else:
#             print("Country not present in dictionary")
#     if x.lower()=='query':
#         country_name=input("Enter the country name you want to query: ")
#         if country_name in country_pop:
#             print(f" Population is: {country_pop[country_name]}")
#         else:
#             print("Such country is not present in dictionary")
            
        
# country_pop()

#solution
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()

    