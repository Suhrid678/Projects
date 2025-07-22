from datetime import datetime
from write import write_to_text

today_date_and_time = datetime.now()

def display_available_lands(land_collection, rented_lands):
    print("\n***********Techno Property Nepal****************\n")
    print("\n*******List of available lands for rent*******\n")
    print("\n***********Techno Property Nepal****************\n")
            
    available_found = False
    print("Kitta Number\tLocation\t\tDirection\tLand Anna\tLand Price\tStatus")
    for land in land_collection:
        if land[-1] == "Available":
            is_rented = any(land in rented_list for rented_list in rented_lands.values())
            if not is_rented:
                available_found = True
                print(land[0] + "\t\t" + land[1] + "\t\t" + land[2] + "\t\t" + land[3] + "\t\t" + land[4] + "\t\t" + land[5])

    if not available_found:
        print("All land is sold")



def rent_land(kitta_num, My_Land, owner_name, duration, rented_lands):
    updated_text = []
    total_cost = 0
    kitta = False
    land_return_info = None
    for land in My_Land:
        if land[0] == str(kitta_num):
            kitta = True
            if land[-1] == "Available":
                while True:
                    conform = input("Please be sure if you want to rent the land as there is no refund policy.(y/n)")
                    if conform.lower() == "y":
                        land[-1] = "Not Available"
                        total_cost += float(land[4]) * duration
                        print("Details of this rent:")
                        print("Location:\t\t" + land[1])
                        print("Land Anna:\t\t" + land[3])
                        print("Rented by:\t\t" + owner_name)
                        print("Total Cost:\t\t" + str(total_cost))
                        print("Direction:\t\t" + land[2])
                        print("Kitta Number:\t\t" + kitta_num)
                        print("Land Price:\t\t" + land[4])


                        if owner_name in rented_lands:
                            rented_lands[owner_name].append(land)
                        else:
                            rented_lands[owner_name] = [land]
                        invoice(land, owner_name, duration)
                        land_return_info = land
                        break
                    elif conform.lower() == "n":
                        print("Canceled")
                        break
                    else:
                        print("Invalid response. Please enter 'y' or 'n'.")
            else:
                print("This land is not available")
        updated_text.append(land)
    if not kitta:
        print("Wrong kitta number")

    write_to_text(updated_text)

    return updated_text, total_cost, land_return_info

def return_land(kitta_num, My_Land, rented_lands):
    updated_text = []
    for land in My_Land:
        if land[0] == str(kitta_num):
            if land[-1] == "Not Available":
                for rented_list in rented_lands.values():
                    if land in rented_list:
                        rented_list.remove(land)
                        land[-1] = "Available"
                        print("Return Details:")
                        print("Land with kitta number " + kitta_num + " has been returned")
                        break
        updated_text.append(land)

    write_to_text(updated_text)

    return updated_text

def invoice(info, owner_name, duration):
    kitta_num = info[0]
    city = info[1]
    direction = info[2]
    area = info[3]
    date_of_rent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_amount = float(info[4]) * duration

    
    invoice_info = "Customer Name: " + owner_name + "\tKitta Number: " + kitta_num + "\n"
    invoice_info += "City/District: " + city + "\tFacing: " + direction + "\n"
    invoice_info += "Land Area(in anna): " + area + "\tRent start date: " + date_of_rent + "\n"
    invoice_info += "Duration(months): " + str(duration) + "\tTotal rental Amount: " + str(total_amount) + "\n"

  
    with open("rented_.txt", "a") as file:
        file.write(invoice_info)
    print("Invoice is generated")

def return_invoice(owner_name, duration, kitta_num, return_back, land_return_info, today_date_and_time):
    print("Return Invoice Details:")
    print("Kitta Number:          " + kitta_num)
    print("Customer Name:         " + owner_name)
    print("City/District:         " + land_return_info[1])
    print("Facing:                " + land_return_info[2])
    print("Land in Anna:          " + land_return_info[3])
    print("Return Date and Time:  " + str(today_date_and_time))
    print("Rent Duration:         " + str(duration) + " months")
    total_amount = float(land_return_info[4]) * duration
    print("Total Amount:          " + str(total_amount))



    if duration < return_back:
        left_month = return_back - duration
        fine = left_month * float(land_return_info[4]) * 0.2
        print("Fine for returning late: ", str(fine))

    invoice_desc = "Return Invoice Details:\n"
    invoice_desc = "Customer Name: " + str(owner_name) + "\tKitta Number: " +str(kitta_num) + "\n"
    invoice_desc += "City/District: " + str(land_return_info[1]) + "\tFacing: " + str(land_return_info[2]) + "\n"
    invoice_desc += "Land Area(in anna): " + str(land_return_info[3]) + "\tReturn date: " + str(today_date_and_time)+ "\n"
    invoice_desc += "Duration(months): " + str(duration) + "\tTotal rental Amount: " + str(total_amount) + "\n"

    if duration < return_back:
        fine = left_month * float(land_return_info[4]) * 0.2
        invoice_desc += "Fine for returning late: " + str(fine) + "\n"

    with open("land_return_report.txt", "a") as file:
        file.write(invoice_desc + "\n")

    print("Return invoice generated successfully.")
