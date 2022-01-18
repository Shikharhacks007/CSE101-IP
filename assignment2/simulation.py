# Name - Shikhar Sharma
# Roll No - 2020121

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.

import a2


def menu():
    print("Hi welcome to our utility tool")
    print("We provide the following tools to use with")
    print("""
    1. read_data_from_file
    2. filter_by_first_name
    3. filter_by_last_name
    4. filter_by_full_name
    5. filter_by_age_range
    6. count_by_gender
    7. filter_by_address
    8. find_alumni
    9. find_topper_of_each_institute
    10. find_blood_donors
    11. get_common_friends
    12. is_related
    13. delete_by_id
    14. add_friend
    15. remove_friend
    16. add_education""")

    print("Please run case:1 before running any cases !!")


def call():
    global records
    while True:
        case = input("Enter the number of the tool you want to use: ")
        if case != "" or case != " ":
            if case != "-1":
                if case == "1":
                    records = a2.read_data_from_file()

                elif case == "2":
                    name_f = input("Please Enter the first Name: ")
                    print(a2.filter_by_first_name(records, name_f))

                elif case == "3":
                    name_l = input("Please Enter the last Name: ")
                    print(a2.filter_by_last_name(records, name_l))

                elif case == "4":
                    f_name = input("Enter the Full name: ")
                    print(a2.filter_by_full_name(records, f_name))

                elif case == "5":
                    min = int(input("Enter the Minimum age: "))
                    max = int(input("Enter the Maximum age: "))
                    print(a2.filter_by_age_range(records, min, max))

                elif case == "6":
                    print(a2.count_by_gender(records))

                elif case == "7":
                    addr = {}
                    house = input("House Number").strip()
                    block = input("Block").strip()
                    town = input("Town").strip()
                    city = input("City").strip()
                    state = input("State").strip()
                    pincode = input("Pincode").strip()
                    if house != "":
                        addr["house_no"] = house
                    if block != "":
                        addr["block"] = block
                    if town != "":
                        addr["town"] = town
                    if city != "":
                        addr["city"] = city
                    if state != "":
                        addr["state"] = state
                    if pincode != "":
                        addr["pincode"] = pincode
                    print(a2.filter_by_address(records, addr))  # need solve

                elif case == "8":
                    inst_name = input("Enter the Institute Name: ")
                    print(a2.find_alumni(records, inst_name))

                elif case == "9":
                    print(a2.find_topper_of_each_institute(records))

                elif case == "10":
                    receive = int(input("Enter the Id of Receiver person's Id: "))
                    print(a2.find_blood_donors(records, receive))

                elif case == '11':
                    a = list(map(int, input("Enter the Id's: ").split()))
                    print(a2.get_common_friends(records, a)) # need to check this

                elif case == '12':
                    person1 = input("Enter the first person: ")
                    person2 = input("Enter the second person: ")
                    print(a2.is_related(records, person1, person2))

                elif case == '13':
                    d = input("Enter the Element to be deleted: ")
                    if d!= "" and d.isdigit() == True:
                        records = a2.delete_by_id(records, int(d))
                        print(records)
                    else:
                        print("Id not found")

                elif case == '14':
                    e = int(input("Person 1: "))
                    f = int(input("Friend 2: "))
                    records = a2.add_friend(records, e, f)
                    print(a2.add_friend(records, e, f))

                elif case == '15':
                    e = int(input("Person 1: "))
                    f = int(input("Friend 1: "))
                    records = a2.remove_friend(records, e, f)
                    print(a2.remove_friend(records, e, f))
                    print("They are deleted now")

                elif case == '16':
                    id = int(input("Person ID: "))
                    institute = input("Institute name: ")
                    ongoing = input("Enter Ongoing Status: ")
                    if ongoing.lower() == "true":
                        ongoing = True
                        percentage = 0.0
                    else:
                        ongoing = False
                        percentage = float(input("Enter Percentage: "))
                    records = a2.add_education(records, id, institute, ongoing, percentage)
                    print(a2.add_education(records, id, institute, ongoing, percentage))

            else:
                print("Thank you for using our tools, have a great day and stay safe!!")
                break

        else:
            print("Enter a Valid integer between 1 and 16")


if __name__ == "__main__":
    menu()
    records = []
    call()