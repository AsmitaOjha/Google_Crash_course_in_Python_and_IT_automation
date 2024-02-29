siblings = ['Prakash','Aastha','Asmita','Kapil']
print('jayanti' in siblings)
print('Prakash' in siblings)
print(type(siblings))
print(len(siblings))
print(siblings[3])
cousins = ['Puja','Sambhu','Annu','Kabir','Assu','Aastha','Kapil','sani']
print(cousins[3:])
print(cousins[:5])

cousins.append('Prakash')
print(cousins)
cousins.pop(3)
print(cousins)
cousins.remove('Assu')
print(cousins)
cousins[5]='Kabir'
print(cousins)
