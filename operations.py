
#a function to create a welcome display message is created.
def welcome_message():
    """A function to display the main heading"""
    print("\n\n\n")
    print("\t\t\t\t\t\t!!!!!!! BABA LAPTOP INDUSTRIES !!!!!!!")
    print("\t\t\t\t\t\t\t\t01-000000")
    print("\t\t\t\t\t\t\t\t Taudaha")
    print("\t\t\t\t\t\t         -----------------------        ")
    print("\n")

#a function to display a heading of the laptop details table
def table_heading():
    """A function to display the heading of the table of laptop data"""
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("ID\t\tLAPTOP NAME\t\tBRAND\t\t\tPRICE\t      QUANTITY\t\tPROCESSOR DETAILS\tGRAPHICS CARD")
    print("---------------------------------------------------------------------------------------------------------------------------------------")


def user_options():
    """A function to display the options to the user to sell, buy and exit."""
    print("\n")
    print("----------------------------------------------------------------")
    print("Please select option 1 to sell laptop to the customer!")
    print("Please select option 2 to purchase laptop from the manufacturer!")
    print("Please select option 3 to exit the system!")
    print("----------------------------------------------------------------")
    print("\n")


 

def option_1_user_details():
    """A function to display a simple message"""
    print("\n")
    print("------------------------------------------------------------")
    print("Please enter the following details to proceed with the order!!!")
    print("------------------------------------------------------------")


def manufacturer_details():
    """A function to ask user input for the manufacturer details and returns values of manufacturer_name,manufacturer_phone_number,manufacturer_address."""
    print("\n")
    print("----------------------------------------------------")
    manufacturer_name = input("Enter the name of the manufacturer: ")
    print("----------------------------------------------------")
    print("\n")
    print("---------------------------------------------------------------")
    manufacturer_phone_number = input("Enter the phone number of the manufacturer: ")
    print("---------------------------------------------------------------")
    print("\n")
    print("-----------------------------------------------------")
    manufacturer_address = input("Enter the address of the manufacturer: ")
    print("-----------------------------------------------------")
    print("\n")
    return manufacturer_name,manufacturer_phone_number,manufacturer_address

def customer_details():
    """A function to ask user input for the customer details and returns values of customer_name,customer_phone_number,customer_address."""
    print("\n")
    print("----------------------------------------------------")
    customer_name = input("Enter the full name of the customer: ")
    print("----------------------------------------------------")
    print("\n")
    print("---------------------------------------------------------------")
    customer_phone_number = input("Enter the phone number of the customer: ")
    print("---------------------------------------------------------------")
    print("\n")
    print("-----------------------------------------------------")
    customer_address = input("Enter the address of the customer: ")
    print("-----------------------------------------------------")
    return customer_name,customer_phone_number,customer_address

   



def purchase_laptop_id_validate(dictionary_data):
    """A function to ask user input for the id of the laptop to buy and validating it also returns value of ID_of_the_laptop_to_be_bought"""
    print("\n")
    id_loop = True
    while id_loop == True:
        try:
            print("---------------------------------------------------------------------------------------")
            ID_of_the_laptop_to_be_bought = int(input("Please enter the ID of the laptop you want to buy: "))
            print("---------------------------------------------------------------------------------------")
            id_loop = False
        except ValueError:
            print("Please provide a valid information")
    print("\n")
    while ID_of_the_laptop_to_be_bought <=0 or ID_of_the_laptop_to_be_bought > len(dictionary_data):
        print("\n")
        print("-----------------------------------------")
        print("Invalid Choice!!!")
        print("Product ID are: 1, 2, 3, 4 and 5 only!!!!")
        print("-----------------------------------------")
        print("\n\n")
        id_loop = True
        while id_loop == True:
            try:
                print("---------------------------------------------------------------------------------------")
                ID_of_the_laptop_to_be_bought = int(input("Please enter the ID of the laptop you want to buy: "))
                print("---------------------------------------------------------------------------------------")
                id_loop = False
            except ValueError:
                print("Please provide a valid information")
    return ID_of_the_laptop_to_be_bought



def purchase_quantity_validate():
    """A function to ask user input for the quantity of the laptop to buy and validating it also returns the value of quantity_of_laptop_to_buy"""
    quantity_loop = True
    while quantity_loop ==True:
        try:
            print("---------------------------------------------------------------------------------------")
            quantity_of_laptop_to_buy = int(input("Enter the quantity of laptop to buy from manufacturer: "))
            print("---------------------------------------------------------------------------------------")
            quantity_loop=False
        except ValueError:
            print("Please provide a valid information")
    while quantity_of_laptop_to_buy <= 0:
        print("\n")
        print("----------------------------------------------")
        print("The quantity you have entered doesn't exist!!!")
        print("Please enter a valid quantity and try again!!!")
        print("----------------------------------------------")
        print("\n\n")
        quantity_loop = True
        while quantity_loop ==True:
            try:
                print("---------------------------------------------------------------------------------------")
                quantity_of_laptop_to_buy = int(input("Enter the quantity of laptop to buy from manufacturer: "))
                print("---------------------------------------------------------------------------------------")
                quantity_loop=False
            except ValueError:
                print("Please provide a valid information")
    return quantity_of_laptop_to_buy



def sales_quantity_validation(quantity_stored_in_dictionary):
    """A function to ask user input for the quantity of the laptop to sell and validating it also returns the value of quantity_of_laptop_to_sell"""
    quantity_1_loop = True
    while quantity_1_loop ==True:
        try:
            print("---------------------------------------------------------------------------------------")
            quantity_of_laptop_to_sell = int(input("Enter the quantity of laptop to sell to the customer: "))
            print("---------------------------------------------------------------------------------------") 
            quantity_1_loop=False
        except ValueError:
            print("Please provide a valid information")
    while quantity_of_laptop_to_sell <= 0 or quantity_of_laptop_to_sell > int(quantity_stored_in_dictionary):
        print("\n")
        print("----------------------------------------------")
        print("The quantity you have entered doesn't exist!!!")
        print("Please enter a valid quantity and try again!!!")
        print("----------------------------------------------")
        print("\n\n")
        quantity_1_loop = True
        while quantity_1_loop ==True:
            try:
                print("---------------------------------------------------------------------------------------")
                quantity_of_laptop_to_sell = int(input("Enter the quantity of laptop to sell to the customer: "))
                print("---------------------------------------------------------------------------------------") 
                quantity_1_loop=False
            except ValueError:
                print("Please provide a valid information")
    return quantity_of_laptop_to_sell



def sales_id_validation(laptop_data_in_dictionary):
    """A function to ask user input for the id of the laptop to sell and validating it also returns values of ID_of_the_laptop_to_be_sold"""
    print("\n")
    sales_id_loop = True
    while sales_id_loop == True:
        try:
    
            print("---------------------------------------------------------------------------------------")
            ID_of_the_laptop_to_be_sold = int(input("Please enter the ID of the laptop you want to sell: "))
            print("---------------------------------------------------------------------------------------")
            sales_id_loop=False
        except ValueError:
            print("Please enter a valid information!")
    print("\n")
    while ID_of_the_laptop_to_be_sold <=0 or ID_of_the_laptop_to_be_sold > len(laptop_data_in_dictionary):
        print("\n")
        print("-----------------------------------------")
        print("Invalid Choice!!!")
        print("Product ID are: 1, 2, 3, 4 and 5 only!!!!")
        print("-----------------------------------------")
        print("\n\n")
        sales_id_loop = True
        while sales_id_loop == True:
            try:
    
                print("---------------------------------------------------------------------------------------")
                ID_of_the_laptop_to_be_sold = int(input("Please enter the ID of the laptop you want to sell: "))
                print("---------------------------------------------------------------------------------------")
                sales_id_loop=False
            except ValueError:
                print("Please enter a valid information!")
    return ID_of_the_laptop_to_be_sold

def purchase_stock_update(dictionary_data,id_of_laptop_to_buy,purchase_quantity):
    """A function to update the stock in the dictionary when user purchase laptops"""
    dictionary_data[id_of_laptop_to_buy][3] = int(dictionary_data[id_of_laptop_to_buy][3])+int(purchase_quantity)

def sales_stock_update(laptop_data_in_dictionary,ID_of_the_laptop_to_be_sold,quantity):
    """A function to update the stock in the dictionary when user sells laptops"""
    laptop_data_in_dictionary[ID_of_the_laptop_to_be_sold][3] = int(laptop_data_in_dictionary[ID_of_the_laptop_to_be_sold][3])-int(quantity)


def invalid_id_of_laptop():
    """A function to display a simple message in case of invalid laptop id"""
    print("\n")
    print("-----------------------------------------")
    print("Invalid Choice!!!")
    print("Product ID are: 1, 2, 3, 4 and 5 only!!!!")
    print("-----------------------------------------")

def invalid_quantity():
    """A function to display a simple message in case of invalid laptop quantity"""
    print("\n")
    print("----------------------------------------------")
    print("The quantity you have entered doesn't exist!!!")
    print("Please enter a valid quantity and try again!!!")
    print("----------------------------------------------")
    print("\n\n")

def print_sales_bill(date_time, customer_name,customer_phone_number,customer_address,laptops_bought_by_customers):
    """A function to display a sales bill when user sells laptops"""
    total = 0
    delivery_charges = 5
    currentTime = date_time.strftime("%H:%M:%S")
    currentDate = date_time.strftime("%d/%m/%Y")
    for price in laptops_bought_by_customers:
        total+= int(price[4])
    grand_total = delivery_charges + total
    #print
    print("\n\n")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t!!!!!!! BABA LAPTOP INDUSTRIES !!!!!!!")
    print("\t\t\t\t\t01-000000")
    print("\t\t\t\t\t Taudaha")
    print("\t\t\t        -----------------------        ")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t\t\tSALES BILL")
    print("---------------------------------------------------------------------------------------")
    print("Date/Time: " +currentDate + " " + currentTime)
    print("---------------------------------------------------------------------------------------")
    print("Customer Details")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("Name of the Customer: " + customer_name)
    print("Phone number of the Customer: " + customer_phone_number)
    print("Address of the Customer: " + customer_address)
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t\t\tItems Purchased")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("Laptop Name \t     Brand \t Quantity \t Price \t     Total Price")
    print("---------------------------------------------------------------------------------------")
    for i in laptops_bought_by_customers:
        print(i[0],"   ",i[1],"     ",i[2],"         ","$",i[3],"       ","$",i[4])
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\tYour total price is:       $", total)
    print("\t\t\t\tYour delivery charges is:  $", delivery_charges)
    print("\t\t\t\tYour grand total price is: $", grand_total)
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\tThank you for transactng with us!!!")
    print("\t\t\t\tWe hope to see you soon again!!!")
    print("\t\t\t\t      Have a good day!!!") 
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\n")

def print_purchase_bill(date_time, manufacturer_name,manufacturer_phone_number,manufacturer_address,laptops_bought):
    """A function to display a purchase bill when user sells laptops"""
    total = 0
    VAT = 0.13
    currentTime = date_time.strftime("%H:%M:%S")
    currentDate = date_time.strftime("%d/%m/%Y")
    for price in laptops_bought:
        total+= int(price[4])
    vat_total = VAT * total
    grand_total = vat_total+ total
    #print
    print("\n\n")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t!!!!!!! BABA LAPTOP INDUSTRIES !!!!!!!")
    print("\t\t\t\t\t01-000000")
    print("\t\t\t\t\t Taudaha")
    print("\t\t\t        -----------------------        ")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t\t\tPURCHASE BILL")
    print("---------------------------------------------------------------------------------------")
    print("VAT: 20001010")
    print("---------------------------------------------------------------------------------------")
    print("Date/Time: " +currentDate + " " + currentTime)
    print("---------------------------------------------------------------------------------------")
    print("Manufacturer Details")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("Name of the Manufacturer: " + manufacturer_name)
    print("Phone number of the Manufacturer: " + manufacturer_phone_number)
    print("Address of the Manufacturer: " + manufacturer_address)
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\t\t\t\t\tItems Purchased")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("Laptop Name \t     Brand \t Quantity \t Price \t     Total Price")
    print("---------------------------------------------------------------------------------------")
    for i in laptops_bought:
        print(i[0],"   ",i[1],"     ",i[2],"         ","$",i[3],"       ","$",i[4])
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\tYour total price is:       $", total)
    print("\t\t\t\tYour VAT amount is:        $", vat_total)
    print("\t\t\t\tYour grand total price is: $", grand_total)
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\tThank you for transactng with us!!!")
    print("\t\t\t\tWe hope to see you soon again!!!")
    print("\t\t\t\t      Have a good day!!!")
    print("\n")
    print("---------------------------------------------------------------------------------------")
    print("\n")

def exit_sys():
    """A function to display a suitable message when user exits the system"""
    print("\n\n")
    print("--------------------------")
    print("You have exited the system!")
    print("Thank You For Your Time!")
    print("Have a good day!")
    print("--------------------------")
