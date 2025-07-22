from operations import *
from read import read_from_text
from datetime import datetime

def main_function():
    My_Land = read_from_text()
    rented_lands = {}
    total_rent_cost = 0

    while True:
        available_land_database = any(land[-1] == "Available" for land in My_Land)

        if not available_land_database:
            print("No land found.")
            break

        display_available_lands(My_Land, rented_lands)
        print()
        while True:
            owner_name = input("Please enter your full name or 'quit': ")
            if owner_name.lower() == 'quit':
                print("Thank you for visiting.")
                break
            elif not owner_name.replace(' ', '').isalpha():
                print("Invalid name. Please enter alphabetic characters only.")
            else:
                 break


        while True:
            user_choice = input("\nType 'rent' to rent land or 'return' to return land: ").lower()

            if user_choice == 'rent':
                kitta_num = input("Please provide the kitta number: ")
                for land in My_Land:
                    if land[0] == kitta_num:
                        if land[-1] == "Available":
                            print("We have " + land[3] + " ana of land available for kitta number " + kitta_num + ".")
                            duration = int(input("Enter the number of months you want to rent the land for: "))
                            My_Land, rental_cost, land_return_info = rent_land(kitta_num, My_Land, owner_name, duration, rented_lands)
                            total_rent_cost += rental_cost
                            print("The total cost turns out to be " + str(total_rent_cost) + ".")
                            break
                        else:
                            print("The land is not available.")
                            break
                else:
                    print("Wrong kitta number.")

            elif user_choice.lower() == 'return':
                kitta_num = input("Please provide the kitta number you want to return: ")
                return_back = int(input("Please enter the number of months you rented the land for: "))

                for land in My_Land:
                    if land[0] == kitta_num:
                        if land[-1] == "Not Available":
                            My_Land = return_land(kitta_num, My_Land, rented_lands)
                            if return_back > 0:
                                print("You have used the land for", return_back, "months.")
                                return_invoice(owner_name, duration, kitta_num, return_back, land, datetime.now())
                            break
                        else:
                            print("The land is not currently rented.")
                            break
                else:
                    print("Wrong kitta number.")

            elif user_choice.lower() == 'quit':
                print("Thank you for your cooperation and support.")
                break

            else:
                print("Wrong choice. Type 'rent' to rent land or 'return' to return land.")

        next_action = input("Do you want to rent more land? Type 'rent' to rent land, 'return' to return land, or 'quit' to exit: ")
        prompt = ["rent", "return", "quit"]
        if next_action.lower() not in prompt:
            print("Wrong input. Type 'rent' to rent land, 'return' to return land, or 'quit' to exit.")
            continue

        if next_action.lower() == 'quit':
            print("Thank you for visiting.")
            break

main_function()
