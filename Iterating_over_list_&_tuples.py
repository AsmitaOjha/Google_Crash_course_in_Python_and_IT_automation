winners = ['Ashley','Dylan','Reese']
for index, person in enumerate(winners):
    print("{} - {}".format(index +1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append('{} <{}>'.format(name,email))
    return result
print(full_emails([('alex@example.com','Alex Diego'),('shay@example.com','Shayre Ojendo')]))