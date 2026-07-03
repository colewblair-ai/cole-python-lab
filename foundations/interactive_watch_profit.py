purchase_price = int(input("Purchase price: "))
sale_price = int(input("Sale price: "))

profit = sale_price - purchase_price

print("Profit:", profit)

if profit > 0:
    print("Good deal")
elif profit < 0:
    print("Bad deal")
else:
    print("Break even")