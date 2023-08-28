# neccessary imports
# global list variable
cart = []

def addItem(item):
    cart.append(item)
    print("{} added succesfully".format(item))
def removeItem(item):
    try:
        cart.remove(item)
        print("{} has been removed succesfully".format(item))
    except:
        print("Sorry, we could not remove the item")
def showCart():
    if cart:
        print("Here is your cart")
        for item in cart:
            print("-{}".format(item))
    else:
        print("Your cart is empty")
def clearCart():
    cart.clear()
    print("Your cart is empty")
def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()
        if ans == 'quit':
            print("Thank you for using our program")
            done = True
        elif ans == 'add':
            item = input("What would you like to add? ").title()
            addItem(item)
        elif ans == 'remove':
            showCart()
            item = input("What item would you like to remove? ").title()
            removeItem(item)
        elif ans == 'show':
            showCart()
        elif ans == 'clear':
            clearCart()
        else:
            print("Sorry, that was not an option")

main()

