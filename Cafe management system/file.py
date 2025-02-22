# Cafe management system
add = []
print("Welcome to our restaurant. Here's the Menu :")
print("Pizza : 30\nPasta : 40\nBurger : 50\nSalad : 60\nCoffee : 70")
dict = {
    "Pizza" : 30,
    "Pasta" : 40,
    "Burgur" : 50,
    "Salad" : 60,
    "Coffee" : 70
}
order_total = 0
item = input("Enter your 1st item you want to order : ")
if item in dict:
    order_total += dict[item]
    add.append(item)
else:
    print("Please write the correct data !")
print(f"Order of {item} has been added.")
data = input("Do you want to add anythings else ?")
if data=="yes":
    item = input("Enter item for 2nd order : ")
    order_total += dict[item]
    add.append(item)
elif data=="no":
    quit
else:
    print("Please write a valid data.")
print("The total price to pay is", order_total)