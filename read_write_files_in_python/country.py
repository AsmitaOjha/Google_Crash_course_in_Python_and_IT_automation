input_filename = 'country_info.txt'
countries = {}
with open(input_filename) as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital,code,code3,dialing,timezone,currency=data
        # print(country, capital,code,code3,dialing,timezone,currency,sep='\n\t')
        country_dict ={
            'name':country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,

        }
        print(country_dict)
        countries[country.casefold()]=country_dict
        countries[code.casefold()]=country_dict
# cd
# print(countries[country])
while True:
    your_country= input("Enter country name: ").casefold()
    if your_country in countries:
        your_country_data=countries[your_country]
        your_capital=your_country_data['capital']
        # print(your_country_data)
        print(f"{your_country}'s capital is: {your_capital}")
    else:
        print("Invalid, please enter proper country name")
        break
        
