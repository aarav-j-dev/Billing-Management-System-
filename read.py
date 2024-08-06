def storing_data_of_file():
    """a function to store in a dictionary and also returns the value of laptop_data"""
    file = open("laptop_data.txt","r")
    laptop_data = {}
    laptop_id = 1
    for values in file:
        values = values.replace("\n","")
        laptop_data.update({laptop_id: values.split(",")})
        laptop_id = laptop_id + 1
    file.close()
    return laptop_data

def display_laptop_data():
    """a function to display the data of the text file"""
    file = open("laptop_data.txt", "r")
    laptop_id = 1
    for values in file:
        print(laptop_id, "\t\t" + values.replace(",","\t\t"))
        laptop_id=laptop_id+1
        print("---------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

