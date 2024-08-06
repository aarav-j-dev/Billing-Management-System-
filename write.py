
def generate_sales_bill(date_time,customer_name,customer_phone_number,customer_address, laptops_bought_by_customers):
    """A function is created to create a text file with date and name of customer where the sales bill is present"""
    total = 0
    delivery_charges = 5
    currentTime = date_time.strftime("%H:%M:%S")
    currentDate = date_time.strftime("%d/%m/%Y")
    current_time = ""
    current_date = ""
    for time in currentTime:
        time = time.replace(":","-")
        current_time +=time
    for date in currentDate:
        date = date.replace("/","-")
        current_date += date
    for price in laptops_bought_by_customers:
        total+= int(price[4])
    grand_total = delivery_charges + total
    file = open("sales" +"_"+customer_name+"_" + current_date+"_"+current_time+".txt","w")
    file.write("\n\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t!!!!!!! BABA LAPTOP INDUSTRIES !!!!!!!\n")
    file.write("\t\t\t\t\t01-000000\n")
    file.write("\t\t\t\t\t Taudaha\n")
    file.write("\t\t\t        -----------------------        \n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\tSALES BILL\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Date/Time: " +current_date + " " + current_time +"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Customer Details\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Name of the Customer: " + customer_name+"\n")
    file.write("Phone number of the Customer: " + customer_phone_number+"\n")
    file.write("Address of the Customer: " + customer_address+"\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\tItems Purchased\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Laptop Name \t     Brand \t Quantity \t Price \t     Total Price\n")
    file.write("---------------------------------------------------------------------------------------\n")
    for i in laptops_bought_by_customers:
        file.write(str(i[0])+"       "+str(i[1])+"     "+str(i[2])+"         "+"$"+str(i[3])+"            "+"$"+str(i[4])+"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\tYour total price is:       $"+ str(total)+"\n")
    file.write("\t\t\t\tYour delivery charges is:  $"+ str(delivery_charges)+"\n")
    file.write("\t\t\t\tYour grand total price is: $"+ str(grand_total)+"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\tThank you for transactng with us!!!\n")
    file.write("\t\t\t\tWe hope to see you soon again!!!\n")
    file.write("\t\t\t\t      Have a good day!!!\n") 
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.close()


 
def generate_purchase_bill(date_time, manufacturer_name,manufacturer_phone_number,manufacturer_address, laptops_bought):
    """A function is created to create a text file with date and name of manufacturer where the purchase bill is present"""
    total = 0
    VAT = 0.13
    currentTime = date_time.strftime("%H:%M:%S")
    currentDate = date_time.strftime("%d/%m/%Y")
    current_time = ""
    current_date = ""
    for time in currentTime:
        time = time.replace(":","_")
        current_time +=time
    for date in currentDate:
        date = date.replace("/","_")
        current_date += date
    for price in laptops_bought:
        total+= int(price[4])
    vat_total = VAT * total
    grand_total = vat_total+ total
    
    file = open("purchase" + "_"+manufacturer_name+"_" + current_date+"_"+current_time+".txt","w")
    file.write("\n\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t!!!!!!! BABA LAPTOP INDUSTRIES !!!!!!!\n")
    file.write("\t\t\t\t\t01-000000\n")
    file.write("\t\t\t\t\t Taudaha\n")
    file.write("\t\t\t        -----------------------        \n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\tPURCHASE BILL\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("VAT: 20001010\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Date/Time: " +current_date + " " + current_time +"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Manufacturer Details\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Name of the Manufacturer: " + manufacturer_name+"\n")
    file.write("Phone number of the Manufacturer: " + manufacturer_phone_number+"\n")
    file.write("Address of the Manufacturer: " + manufacturer_address+"\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\tItems Purchased\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("Laptop Name \t     Brand \t Quantity \t Price \t     Total Price\n")
    file.write("---------------------------------------------------------------------------------------\n")
    for i in laptops_bought:
        file.write(str(i[0])+"       "+str(i[1])+"     "+str(i[2])+"         "+"$"+str(i[3])+"           "+"$"+str(i[4])+"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\tYour total price is:       $"+ str(total)+"\n")
    file.write("\t\t\t\tYour VAT amount is:        $"+ str(vat_total)+"\n")
    file.write("\t\t\t\tYour grand total price is: $"+ str(grand_total)+"\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\tThank you for transactng with us!!!\n")
    file.write("\t\t\t\tWe hope to see you soon again!!!\n")
    file.write("\t\t\t\t      Have a good day!!!\n") 
    file.write("---------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.close()

def purchase_stock_update_in_file(dictionary_data):
    """A function to update the stock information in the text file when the user purchase laptops."""
    file = open("laptop_data.txt","w")
    for value in dictionary_data.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4])+","+str(value[5]))
        file.write("\n")
    file.close()

def sales_stock_update_in_file(laptop_data_in_dictionary):
    """A function to update the stock information in the text file when the user sells laptops."""
    file = open("laptop_data.txt","w")
    for value in laptop_data_in_dictionary.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4])+","+str(value[5]))
        file.write("\n")
    file.close()
    

    
