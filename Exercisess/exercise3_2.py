stock = {
    'info' :[600,630,620],
    'ril':[1430,1490,1567],
    'mtl':[234,180,160]
}

def print_ALL():
    for key,value in stock.items():
        average=sum(value)/len(value)
        print(f'{key}==> {value} ==> age: {round(average,2)}')

def add():
    stock_ticket, price = input("Enter stock ticker and price (ticket,price):  ").split(",")
    price = int(price)

    if stock_ticket in stock:
        stock[stock_ticket].append(price)

    else:
        stock[stock_ticket]=[price]
    print_ALL()


def main():
    op=input("Enter operation(print, add): ")
    if op.lower()=='print':
        print_ALL()
    elif op.lower()=='add':
        add()

if __name__=='__main__':
    main()

#solution from the github exercise series:
# import statistics

# stocks = {
#     'info': [600,630,620],
#     'ril': [1430,1490,1567],
#     'mtl': [234,180,160]
# }

# def print_all():
#     for stock,price_list in stocks.items():
#         avg = statistics.mean(price_list)
#         print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))


# def add():
#     s = input("Enter a stock ticker to add:")
#     p = input("Enter price of this stock:")
#     p=float(p)
#     if s in stocks:
#         stocks[s].append(p)
#     else:
#         stocks[s] = [p]
#     print_all()


# def main():
#     op=input("Enter operation (print, add or amend):")
#     if op.lower() == 'print':
#         print_all()
#     elif op.lower() == 'add':
#         add()
#     else:
#         print("Unsupported operation:",op)

# if __name__ == '__main__':
#     main()