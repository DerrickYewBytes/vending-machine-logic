## Vending Machine Logic
# You are tasked to code the vending machine logic out using Python Programming Language. 
# In your code, you can have a few drinks as your items with any price (no coin). 
# The customer should be able to insert any notes to buy his preferred drinks. 
# The outcome is to release the least amount of notes back to the customer. 

from tabulate import tabulate
import json

def main():
    print("Welcome to ABC Vending Machine")
    displayProducts()
    choice = input("What would you like to order? Select the number from the following list:")
    change = displayProductPrice(choice)
    
    displayChange(change)


product_lists = [{
    "id" : 1,
    "name": "Coca Cola",
    "price": 3
}, {
    "id" : 2,
    "name": "Sprite",
    "price": 4
}, {
    "id" : 3,
    "name": "Pepsi",
    "price": 7
}]

def displayProducts():
    display_header = ["number", "name", "price"]
    display_list = []
    display_list.insert(0,display_header)
    
    #Append all product details into a flat list for tabulate
    for product in product_lists:
        pro_flattened_arr = []
        for value in product.values():
            pro_flattened_arr.append(value)
        display_list.append(pro_flattened_arr)

    print(tabulate(display_list))

def displayProductPrice(choice_id):
    # Check input is number type
    try:
        choice_id = int(choice_id)
    except ValueError:
        raise Exception("Please key in correct id of product")
    
    # Check input is within product list
    if choice_id < 1 or choice_id > product_lists.__len__():
        raise Exception("Please key in correct id of product from the list")
    else: 
        product_price = None
        for product in product_lists:
            if product.get("id") == choice_id:
                product_price = product.get("price")
                break    
        if product_price == None:
            raise Exception("Product not found in the list")
        
        price_paid = input(f"The price is {product_price}, how much are you paying? ")
        change = int(price_paid) - product_price
        return change

def displayChange(change):
    # RM notes consists of 100, 50, 20, 10 ,5, 1
    # Cascade check on each note
    original_change = change
    
    note_amount = {
        100 : 0,
        50 : 0,
        20 : 0,
        10 : 0,
        5 : 0,
        1 : 0
    }
    
    for note in note_amount:
        # Floor division to get number of notes
        count = change // note
        # Update number of notes
        note_amount[note] = count
        # Update latest change
        change %= note
    
    print(f"The change for your payment: {original_change}")
    
    display_header = ["Ringgit Note", "Number"]
    display_list = []
    display_list.insert(0,display_header)
    for note in note_amount:
        flattened_note = [note, note_amount[note]]
        display_list.append(flattened_note)
    print(tabulate(display_list))


main()