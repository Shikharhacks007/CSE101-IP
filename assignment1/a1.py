'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''


def show_menu():
    print('''
    == == == == == == == == == == == == == == == == == == == == == == == == =
                                    MY 	BAZAAR
    == == == == == == == == == == == == == == == == == == == == == == == == =
    Hello! Welcome to my grocery store!
    Following are the products available in the shop:
    
    -------------------------------------------------
    CODE | DESCRIPTION | CATEGORY    | COST(Rs)
    -------------------------------------------------
    0    | Tshirt      | Apparels    | 500
    1    | Trousers    | Apparels    | 600
    2    | Scarf       | Apparels    | 250
    3    | Smartphone  | Electronics | 20,000
    4    | iPad        | Electronics | 30,000
    5    | Laptop      | Electronics | 50,000
    6    | Eggs        | Eatables    | 5
    7    | Chocolate   | Eatables    | 10
    8    | Juice       | Eatables    | 100
    9    | Milk        | Eatables    | 45
    ------------------------------------------------
    ''')


def get_regular_input():
    '''
    Description: Takes space separated item codes (only integers allowed).
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print('''-------------------------------------------------
                  ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------''')

    print("Enter the item codes (space-separated): ")
    temp = input().split()
    item_codes = [0] * 10
    error = 0
    for i in range(0, len(temp)):
        if (temp[i].isdigit() == True) and (int(temp[i]) >= 0):
            item_codes[int(temp[i])] += 1
        else:
            error += 1
    if error >= 1:
        print("There was an error in the input,the corrected values were taken into account")

    item_codes = list(map(int, item_codes))
    print(item_codes)
    return item_codes


def get_bulk_input():
    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer.
    For details, refer PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print('''-------------------------------------------------
            ENTER ITEM AND QUANTITIES
-------------------------------------------------''')
    item_codes = []
    temp = input("Enter code and quantity(leave blank to stop): ")
    item_codes = [0] * 10
    while True:
        if temp == "" or temp == " ":
            break

        else:
            value = temp.split()
            if (0 <= int(value[0]) < 10) and (value[1].isdigit()):
                print(("You added {} " + "{}").format(value[1], items[int(value[0])]))
                item_codes[int(value[0])] += int(value[1])
            elif int(value[0]) > 9 and int(value[1]) > 0:
                print("Invalid code. Try again.")
            elif int(value[1]) < 0 and int(value[0]) <= 9:
                print("Invalid quantity. Try again.")
            elif (value[0]<0 and value[1]<0):
                print("Invalid code and quantity. Try again.")

        temp = input("Enter code and quantity(leave blank to stop): ")

    print(item_codes)
    return item_codes


def print_order_details(quantities):
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: No return value
    '''

    print('''-------------------------------------------------
                ORDER DETAILS
-------------------------------------------------''')

    index = 1
    for i in range(0, len(quantities)):
        if quantities[i] != 0:
            print(("[{}]" + "{} " + "x " + "{}" + " = Rs " + "{}" + "*" + "{}" + "= Rs" + "{}").format(index, items[i],
                                                                                                       quantities[i],
                                                                                                       price[i],
                                                                                                       quantities[i],
                                                                                                       price[i] *
                                                                                                       quantities[i]))
            index += 1


def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: A 3-tuple of integers in the following format:
    (apparels_cost, electronics_cost, eatables_cost)
    '''

    print('''-------------------------------------------------
                CATEGORY-WISE COST
-------------------------------------------------''')
    apparels = 500 * quantities[0] + 600 * quantities[1] + 250 * quantities[2]
    electronics = 20000 * quantities[3] + 30000 * quantities[4] + 50000 * quantities[5]
    eatables = 5 * quantities[6] + 10 * quantities[7] + 100 * quantities[8] + 45 * quantities[9]
    if apparels != 0:
        print("Apparels = Rs " + str(apparels))
    if electronics != 0:
        print("Electronics = Rs " + str(electronics))
    if eatables != 0:
        print("Eatables = Rs " + str(eatables))
    return apparels, electronics, eatables


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''

    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 3-tuple of integers in the following format:
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    '''

    print('''-------------------------------------------------
                    DISCOUNTS
-------------------------------------------------
    ''')
    total_cost = apparels_cost + electronics_cost + eatables_cost
    total_dis = 0
    discounted_apparels_cost = 0
    discounted_electronics_cost = 0
    discounted_eatables_cost = 0
    if apparels_cost >= 2000 and apparels_cost > 0:
        print("[APPAREL] Rs " + "{}".format(apparels_cost) + "-", end="")
        print(get_discount(apparels_cost, 0.1), end=" ")
        total_dis += get_discount(apparels_cost, 0.1)
        discounted_apparels_cost = apparels_cost - get_discount(apparels_cost, 0.1)
        print("Rs " + str(discounted_apparels_cost))
    else:
        discounted_apparels_cost = apparels_cost

    if electronics_cost >= 25000 and electronics_cost > 0:
        print("[ELECTRONICS] Rs " + "{}".format(electronics_cost) + "-", end="")
        print(get_discount(electronics_cost, 0.1), end=" ")
        total_dis += get_discount(electronics_cost, 0.1)
        discounted_electronics_cost = electronics_cost - get_discount(electronics_cost, 0.1)
        print("Rs " + str(discounted_electronics_cost))

    else:
        discounted_electronics_cost = electronics_cost

    if eatables_cost >= 500 and eatables_cost > 0:
        print("[EATABLES] Rs " + "{}".format(eatables_cost) + "-", end="")
        print(get_discount(eatables_cost, 0.1), end=" ")
        total_dis += get_discount(eatables_cost, 0.1)
        discounted_eatables_cost = eatables_cost - get_discount(eatables_cost, 10)
        print("Rs " + str(discounted_eatables_cost))
    else:
        discounted_eatables_cost = eatables_cost

    print("\n" + "TOTAL DISCOUNT = Rs " + str(total_dis))
    print("TOTAL COST = Rs " + str(total_cost - total_dis))

    return discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''

    print('''-------------------------------------------------
                        TAX
-------------------------------------------------''')
    print(("[APPAREL] Rs " + "{}" + " * " + "{}" + "= Rs " + "{}").format(apparels_cost, 0.10,
                                                                          get_tax(apparels_cost, 0.10)))
    print(("[ELECTRONICS] Rs " + "{}" + " * " + "{}" + "= Rs " + "{}").format(electronics_cost, 0.15,
                                                                              get_tax(electronics_cost, 0.15)))
    print(("[Eatables] Rs " + "{}" + " * " + "{}" + "= Rs " + "{}").format(eatables_cost, 0.05,
                                                                           get_tax(eatables_cost, 0.05)))
    total_tax = get_tax(apparels_cost, 0.10) + get_tax(electronics_cost, 0.15) + get_tax(eatables_cost, 0.05)
    total_cost_including_tax = apparels_cost + electronics_cost + eatables_cost + total_tax
    print("\n" + "TOTAL TAX = Rs " + str(total_tax))
    print("TOTAL COST = Rs " + str(total_cost_including_tax))

    return total_cost_including_tax, total_tax


def apply_coupon_code(total_cost):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive).
    For details, refer the PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: The total cost (integer) on which the coupon is to be applied.

    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print('''-------------------------------------------------
                COUPON CODE
-------------------------------------------------''')
    coupon = input("Enter coupon code (else leave blank): ")
    total_coupon_discount = 0
    total_cost_after_coupon_discount = 0
    while True:
        if coupon == "HELLE25":
            if total_cost >= 25000:
                total_coupon_discount = min(5000, total_cost * 0.25)
                print(("[HELLE25] min(5000, Rs {} * 0.25) = Rs {}").format(total_cost, total_coupon_discount))
                print(("TOTAL COUPON DISCOUNT = Rs {}").format(total_coupon_discount))
                total_cost_after_coupon_discount = total_cost-total_coupon_discount
                print(("TOTAL COST = Rs {}").format(total_cost_after_coupon_discount))
                break
            else:
                print("TOTAL COUPON DISCOUNT = Rs " + str(0))
                print("TOTAL COST = Rs " + str(total_cost))
                break

        elif coupon == "CHILL50":
            if total_cost >= 50000:
                total_coupon_discount = min(10000, total_cost * 0.50)
                print(("[CHILL50] min(10000, Rs {} * 0.50) = Rs {}").format(total_cost, min(10000, total_cost * 0.50)))
                print(("TOTAL COUPON DISCOUNT = Rs {}").format(total_coupon_discount))
                total_cost_after_coupon_discount = total_cost - total_coupon_discount
                print(("TOTAL COST = Rs {}").format(total_cost_after_coupon_discount))
                break
            else:
                print("TOTAL COUPON DISCOUNT = Rs " + str(0))
                print("TOTAL COST = Rs " + str(total_cost))
                break

        elif coupon == "" or coupon == " ":
            print("No coupon code applied.\n")
            print("TOTAL COUPON DISCOUNT = Rs " + str(0))
            print("TOTAL COST = Rs " + str(total_cost))
            total_cost_after_coupon_discount = total_cost
            break

        else:
            print("Invalid coupon code.Try again.\n")
            coupon = input("Enter coupon code (else leave blank): ")

    return total_cost_after_coupon_discount, total_coupon_discount


def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate
    print statements to match the output with the screenshots provided in the PDF.

    Parameters: No parameters

    Returns: No return value
    '''

    show_menu()
    while True:
        decesion = input("Would you like to buy in bulk?(y or Y / n or N)")
        if decesion == "y" or decesion == "Y":
            temp_quantities = get_bulk_input()
            print_order_details(temp_quantities)
            category_price = calculate_category_wise_cost(temp_quantities)
            temp_a, temp_b, temp_c = calculate_discounted_prices(category_price[0], category_price[1],
                                                                 category_price[2])
            temp_total_cost_including_tax, temp_total_tax = calculate_tax(temp_a, temp_b, temp_c)
            apply_coupon_code(temp_total_cost_including_tax)
            print("\nThank you for visiting!")
            break

        elif decesion == "n" or decesion == "N":
            temp_quantities = get_regular_input()
            print_order_details(temp_quantities)
            category_price = calculate_category_wise_cost(temp_quantities)
            temp_a, temp_b, temp_c = calculate_discounted_prices(category_price[0], category_price[1],
                                                                 category_price[2])
            temp_total_cost_including_tax, temp_total_tax = calculate_tax(temp_a, temp_b, temp_c)
            apply_coupon_code(temp_total_cost_including_tax)
            print("\nThank you for visiting!")
            break

        else:
            continue


if __name__ == '__main__':
    items = ["Tshirt", "Trousers", "Scarf", "Smartphone", "iPad", "Laptop", "Eggs", "Chocolate", "Juice", "Milk"]
    price = [500, 600, 250, 20000, 30000, 50000, 5, 10, 100, 45]
    category = ["Apparels", "Electronics", "Eatables"]
    main()