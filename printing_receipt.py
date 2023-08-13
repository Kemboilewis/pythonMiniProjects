# products
product_1, price_1 = "Computer CPU ", 50.0
product_2, price_2 = "Monitor ", 20.8
product_3, price_3 = "Books ", 18.7

# company info
company_name = "kenya Tours company Limited"
company_address = "892 Eldama Ravine"
company_city = "Nairobi Kenya"

# ending message
message = "Thanks for shopping with us today!"

print("*"*50)
print("\t\t{} ".format(company_name))
print("\t\t{} ".format(company_address))
print("\t\t{} ".format(company_city))

print("="*50)
print("\tProduct Name \t\tProduct Price")

# print statement for each product
print("\t{}\t\t\t${}".format(product_1.title(), price_1))
print("\t{}\t\t\t${}".format(product_2.title(), price_2))
print("\t{}\t\t\t${}".format(product_3.title(), price_3))

print("="*50)
print("\t\tTotal")
total = price_1 + price_2 + price_3
print("\t\t\t${}".format(total))
print("="*50)

print("\n\t{}\n".format(message))

print("*"*50)
