file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)
  print(file_counts[extension])

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount,ext))

print(file_counts.keys())
print(file_counts.values())
 
def count_letters(text):
  result ={}
  for letter in text:
    if letter not in result:
      result[letter]=0
    result[letter]= result[letter]+1
  return result 

print(count_letters('asmitaojha'))
print(count_letters("rohitpal"))

