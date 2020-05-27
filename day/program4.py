costprice=float(input("Enter Cost Price"))
sellprice=float(input("Enter Selling Price"))
profit=sellprice-costprice
print("Profit: ", profit)
newSellingPrice=1.05*profit+sellprice-profit
print("NewSellingPrice: ",newSellingPrice)

