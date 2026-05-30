snack_name  = "chips"  # str   — text
price       = 1.50     # float - decimal
quantity    =10        # int - whole number
is_available =True     # bool - true or false

print("snack:", snack_name)
print("price:", price)
print("quantity:", quantity)
print("available:", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("total value:$", total)
print("sale price:$", price=0.25)
print("double stock:", quantity * 2)


print("is price under two dollers?", price < 2)
print("more than 5 in stock?", quantity > 5)
print("is price exaxctly 1.50?", price == 1.50)


shop_name = "quick" + " " + "bites"
print("shop name:", shop_name)
print("letters in snack name:", len(snack_name))
print("first letter:", snack_name[0])
