import datetime
from operations import * 
from read import *
from write import * 

date_time = datetime.datetime.now()

#using further codes in a loop so the code isn't terminated until the user demands so by giving 3 as a user input
continue_loop = True
while continue_loop == True:
    #calling function welcome_message to display first welcome message
    welcome_message()
    print("\n")

    #callling function to store the values in the file in a dictionary
    storing_data_of_file()

    #Calling function to display the data in the files and heading
    table_heading()
    display_laptop_data()

    #calling function to display the options
    user_options()

    #asking for input for the option
    print("\n")
    option_loop = True
    while option_loop  == True:
        try:
            user_option_reply = int(input("Please enter the option to continue further: "))
            option_loop = False
        except ValueError:
            print("Please provide a valid information")
    print("\n")


    if user_option_reply == 1:
        #heading
        print("\n")
        print("\n")
        print("\t\t\t\t\t\t\tWelcome to Sales")
        print("\t\t\t\t\t\t\t----------------")
        print("\n")
        
        #customer details input
        customer_name,customer_phone_number,customer_address = customer_details()
        
        #appending the details of the laptops bought by customers in a list
        laptops_bought_by_customers = []

        #running loop
        sell_more = True
        while sell_more == True:
            #displays heading of the table
            table_heading()
            
            #displays data of the table
            display_laptop_data()

            #asking user for the ID of the laptop to be sold and validating the ID of the laptop present in the dictionary
            laptop_data_in_dictionary = storing_data_of_file()
            ID_of_the_laptop_to_be_sold = sales_id_validation(laptop_data_in_dictionary)

            #checking stock zero or not in the dictionary
            if int(laptop_data_in_dictionary[ID_of_the_laptop_to_be_sold][3]) == 0:
                print("\n\n")
                print("Sorry! The laptop you are trying to sell to the customer is currently out of stock!")
                print("\n\n")
                continue

            else:
                #asking user for the quantity to sell to customer and validating quantity as in dictionary
                quantity_stored_in_dictionary = storing_data_of_file()[ID_of_the_laptop_to_be_sold][3]
                quantity = sales_quantity_validation(quantity_stored_in_dictionary)
                
                #update stock
                sales_stock_update(laptop_data_in_dictionary,ID_of_the_laptop_to_be_sold,quantity)
                sales_stock_update_in_file(laptop_data_in_dictionary)
               
                #pricing
                total = int(storing_data_of_file()[ID_of_the_laptop_to_be_sold][2].replace("$",''))*int(quantity)
                laptops_bought_by_customers.append([storing_data_of_file()[ID_of_the_laptop_to_be_sold][0],storing_data_of_file()[ID_of_the_laptop_to_be_sold][1], quantity, storing_data_of_file()[ID_of_the_laptop_to_be_sold][2].replace("$",''),total])
                #arranged in this format(name,brand , quantity, unit price,total price)

                #running loop to ask if user wants to sell again 
                print("\n")
                print("---------------------------------------------------------------------------------------")
                sell_more1 = input("Do you want to add more laptops? Enter Y to continue or any key to print the bill ").upper()
                print("---------------------------------------------------------------------------------------")
                if sell_more1 == "Y":
                    sell_more=True
                    
                else:
                    #bill printing
                    print_sales_bill(date_time, customer_name,customer_phone_number,customer_address, laptops_bought_by_customers)

                    #write a text file with sales bill
                    generate_sales_bill(date_time, customer_name,customer_phone_number,customer_address, laptops_bought_by_customers)
                    
                    #loop handling
                    print("---------------------------------------------------------------------------------------")
                    ask_user = input("Type OK to return back to the system: ").upper()
                    print("---------------------------------------------------------------------------------------")
                    while ask_user != "OK":
                        print("---------------------------------------------------------------------------------------")
                        ask_user = input("Type OK to return back to the system: ").upper()
                        print("---------------------------------------------------------------------------------------")

                    #return to system
                    if ask_user == "OK":
                        sell_more = False
 
    #option 2    
    elif user_option_reply ==2:
        #displays heading
        #heading
        print("\n")
        print("\n")
        print("\t\t\t\t\t\t\tWelcome to Purchase")
        print("\t\t\t\t\t\t\t-------------------")
        print("\n")
        
        #customer details input
        manufacturer_name, manufacturer_phone_number, manufacturer_address = manufacturer_details()

        #appending the details of the laptops bought in a list by creating an empty list
        laptops_bought = []
        buy_more = True
        while buy_more == True:
            #displays heading of the table
            table_heading()

            #displays data of the table
            display_laptop_data()
           
            #asks id of the laptop and validating the ID of the laptop present in the dictionary 
            dictionary_data = storing_data_of_file()
            id_of_laptop_to_buy = purchase_laptop_id_validate(dictionary_data)
            
            #ask quantity to user to buy and vlidating it
            purchase_quantity = purchase_quantity_validate()
            
            #update stock
            purchase_stock_update(dictionary_data,id_of_laptop_to_buy,purchase_quantity)
            purchase_stock_update_in_file(dictionary_data)
            
            #pricing
            total = int(dictionary_data[id_of_laptop_to_buy][2].replace("$",''))*int(purchase_quantity)
            laptops_bought.append([dictionary_data[id_of_laptop_to_buy][0],dictionary_data[id_of_laptop_to_buy][1], purchase_quantity, dictionary_data[id_of_laptop_to_buy][2].replace("$",''),total])

            print("\n")
            print("---------------------------------------------------------------------------------------")
            buy_more1 = input("Do you want to add more laptops? Enter Y to continue or press any key to print the bill").upper()
            print("---------------------------------------------------------------------------------------")
            if buy_more1 == "Y":
                buy_more=True   
            else:
                #print bill
                print_purchase_bill(date_time, manufacturer_name,manufacturer_phone_number,manufacturer_address,laptops_bought)

                #write a text file to generate purchase bill
                generate_purchase_bill(date_time, manufacturer_name,manufacturer_phone_number,manufacturer_address, laptops_bought)
                print("\n")
                print("---------------------------------------------------------------------------------------")
                ask_user = input("Type OK to return back to the system: ").upper()
                print("---------------------------------------------------------------------------------------")
                while ask_user != "OK":
                    print("---------------------------------------------------------------------------------------")
                    ask_user = input("Type OK to return back to the system: ").upper()
                    print("---------------------------------------------------------------------------------------")
                if ask_user == "OK":
                    buy_more = False
                
    #option 3
    elif user_option_reply ==3:
        continue_loop = False
        exit_sys()

    else:
        print("\n")
        print("-----------------------------------------")
        print("Invalid Choice!!!")
        print("Choices are: 1, 2, 3 only!!!!")
        print("-----------------------------------------")
        print("\n")
        continue_loop = True
