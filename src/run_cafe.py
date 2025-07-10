#!/usr/bin/env python


''' 
--- Py script to serve a food delivery business ---
'''


# Set compute environment
import csv
from sys import stdout
from input_idx_test import * # tester_phone_no_input, tester_price_input, tester_idx_input
from utility import *


'''
functions included in the utility module:
save_orders_csv
save_couriers_csv
save_products_csv 
save_products_txt
save_couriers_txt 
load_database_to_CSVs
initial_CSVs_push_to_database,
updated_entities_push_to_database
updated_entities_to_orders_table
load_database_to_CSVs
load_products_txt
load_couriers_txt
load_products_csv
load_couriers_csv
load_porders_csv
'''


# Initial CSVs data loading to database
# Initial_CSVs_push_to_database()  #           <- database rescue func


## Load database tables to CSVs
load_database_to_CSVs()           #           <- load database to CSVs 


#### Functions to load CSVs or txt-s to miniproject.py variables #####
couriers      = load_couriers_txt()
cafe_products = load_products_txt()
products_list = load_products_csv()
couriers_list = load_couriers_csv()
orders_list   = load_orders_csv()


# Create order status list
order_status = ['preparing', 'delivered', 'cancelled']


## MAIN MENU ##
print('\n*** Main menu ***')
hub_menu = int(input("Select 0 to exit program\nSelect 1 for products menu\nSelect 2 for couriers options \
\nSelect 3 for orders options\nYour selection? "))


# PRODUCT MENU
while hub_menu:
    if hub_menu == 1:

        # print products menu
        print('\n* Products menu *:')
        products_menu = int(input("Press 0 to get to main menu, 1 to see menu, 2 to add to the menu, \
        3 to update menu, 4 to delete product from menu: "))

        while products_menu:
            if products_menu == 1:
                print('\nmenu:',cafe_products)

            # add new product
            elif products_menu == 2:
                added_product = input("\nPlease add product to the drinks list: ")
                added_product_price = input("\nPlease add price of the drink: ")
                cafe_products.append(added_product)
                print('Extended menu:',cafe_products)
                product_data = {}
                product_data['name'] = added_product
                product_data['price'] = added_product_price
                products_list.append(product_data)

                # persist record addition to database
                updated_entities_push_to_database(None, added_product, None, added_product_price, None)

            # update products
            elif products_menu == 3:
                for index,product in enumerate(cafe_products):
                    print(f'index = {index} -> {product}')

                # iterate for valid input (to defeat NameError!)
                index_updated_product = tester_idx_input(len(cafe_products))

                # generate new product record
                new_product = input("Input name of new product or hit Enter to reprice existing one: ")
                old_product = products_list[index_updated_product]['name'] 
                old_price = products_list[index_updated_product]['price']
                if new_product != '':
                    cafe_products[index_updated_product] = new_product
                    products_list[index_updated_product]['name'] = new_product
                    price = tester_price_input(new_product)
                    products_list[index_updated_product]['price'] = price
                else:
                    new_product = old_product
                    updated_price = tester_price_input(cafe_products[index_updated_product])
                    products_list[index_updated_product]['price'] = updated_price
                print('Updated products list:',cafe_products)
                print('\nUpdated products menu:',products_list)

                # persist record update to database
                updated_entities_push_to_database(old_product, new_product, float(old_price), float(updated_price), None)

            # remove products
            elif products_menu == 4:
                print('\nmenu',cafe_products)
                for index,product in enumerate(cafe_products):
                    print(f'index = {index} -> {product}')

                # test for valid input (loop to defeat NameError!)
                index_updated_product = tester2_idx_input(len(cafe_products))  # sort out ...test.py and blank input
                
                # generate new product record
                old_product = products_list[index_updated_product]['name'] 
                old_price = products_list[index_updated_product]['price'] 
                new_price=None
                remove_product = cafe_products[index_updated_product]
                cafe_products.remove(remove_product)
                print('Reduced products menu:',cafe_products)
                products_list.pop(index_updated_product)
                print('n\Reduced products list',products_list)

                # persist record deletion to database
                updated_entities_push_to_database(old_product, None, old_price, new_price, None)
            else:
                print("Invalid menu option. Please enter a valid option.")  
                break
            print('\n* Products menu *:')
            products_menu = int(input("Press 0 to get to main menu, 1 to see menu, 2 to add to the menu,\
            3 to update menu, 4 to delete product from menu: "))
    

    # COURIERS OPTIONS
    if hub_menu == 2:   

        # print couriers_data
        print('\n* Couriers menu *:')
        couriers_menu = int(input("\nPress 0 to go to the main menu, 1 to see couriers, 2 to add new courier,\
        3 to update courier, 4 to delete courier: "))

        while couriers_menu:
            if couriers_menu == 1:
                print('\ncouriers:',couriers)

            # add new courier
            elif couriers_menu == 2:
                added_courier = input("\nPlease add a courier to the couriers list: ")
                added_courier_phone = input("\nPlease add the courier's phone: ")
                couriers.append(added_courier)
                print('extended courier list:',couriers)
                courier_data = {}
                courier_data['name'] = added_courier
                courier_data['phone'] = added_courier_phone
                couriers_list.append(courier_data)

                # persist record addition to database
                updated_entities_push_to_database(None, added_courier, None, int(added_courier_phone), case = couriers)

            # update couriers
            elif couriers_menu == 3:
                print('\nIndex:       Courier:')
                for index, courier in enumerate(couriers):
                    print(f'index = {index} -> {courier}')
                # iterate for valid input (to defeat NameError!)
                index_updated_courier = tester_idx_input(len(couriers))

                # generate new courier record
                new_courier = input("Input name of new courier or hit Enter to change their phone: ")
                old_courier = couriers_list[index_updated_courier]['name'] 
                old_phone = couriers_list[index_updated_courier]['phone'] 
                if new_courier != '':
                    couriers[index_updated_courier] = new_courier
                    couriers_list[index_updated_courier]['name'] = new_courier
                    updated_phone = tester_phone_no_input(new_courier)# <- fix input type
                    couriers_list[index_updated_courier]['phone'] = updated_phone
                else:
                    new_courier = old_courier
                    updated_phone = tester_phone_no_input(couriers[index_updated_courier])
                    couriers_list[index_updated_courier]['phone'] = updated_phone
                print("Updated couriers list:", couriers)
                print('\nUpdated courier selection:',couriers_list)

                # persist record update to database
                updated_entities_push_to_database(old_courier, new_courier, int(old_phone), int(updated_phone), case = couriers)

            # remove couriers
            elif couriers_menu == 4:
                print('\nCouriers:',couriers)
                for index,courier in enumerate(couriers):
                    print(f'index = {index} -> {courier}')
                # test for valid input (loop to defeat NameError!)
                index_updated_courier = tester2_idx_input(len(couriers)) 

                # generate new courier record
                old_courier = couriers_list[index_updated_courier]['name'] 
                old_phone = couriers_list[index_updated_courier]['phone'] 
                new_phone=None
                remove_courier = couriers[index_updated_courier]
                couriers.remove(remove_courier)
                print('Reduced couriers menu:',couriers)
                couriers_list.pop(index_updated_courier)
                print('n\Reduced couriers list',couriers_list)

                # persist drecord election to database
                updated_entities_push_to_database(old_courier, None, old_phone, new_phone, case = couriers)
            else:
                print("Invalid menu option. Please enter a valid option.")
                break
            print('\n* Couriers menu *:')
            couriers_menu = int(input("Press 0 to go to the main menu, 1 to see couriers, 2 to add new courier,\
            3 to update courier, 4 to delete courier: "))
    
    
    # ORDER OPTIONS
    elif  hub_menu == 3:

        # print orders options
        print('\n* Orders menu *:\n')
        orders_menu_opt = int(input("Press 0 to go to main menu , 1 to see order data, 2 to add an order, \
        3 to update order status, 4 to update order,  5 to delete order, 6 to show orders list by order status: "))
        while orders_menu_opt:

            # show current orders
            if orders_menu_opt == 1:

                # show orders by index
                print('\nOrders list:\n')
                [print(f'index {el}\n{orders_list[el]}\n') for el in range(len(orders_list))]
            
            # add a new order
            elif orders_menu_opt == 2:
                name_data = input('Enter name: ')
                address_data = input('Enter address: ')
                tel_number_data = int(input('Enter telephone number: '))
                
                # order_status = input('Enter either: preparing, delivered or cancelled')
                print('\nCouriers:',couriers)
                for index, guy in enumerate(couriers):
                    print(f'index = {index} -> {guy}')
                index_courier = tester_idx_input(len(couriers))  # -> ''
                
                # accept new order of products
                for index,product in enumerate(cafe_products):
                    print(f'index = {index} -> {product}')
                customer_ordered = str(input("Enter products indexes separated by comma & space: "))
                while len(list(set(list(customer_ordered.split())))) > len(cafe_products):
                    customer_ordered = str(input("It's too many - enter products indexes separated by comma: "))
                customer_ordered.replace(" ", "")
                order_data = {}
                order_data['customer_name'] = name_data
                order_data['customer_address'] = address_data
                order_data['customer_phone'] = tel_number_data
                order_data['courier'] = index_courier
                order_data['order_status'] = 'preparing'
                order_data['items'] = customer_ordered 
                print('\nnew order:', order_data)
                orders_list.append(order_data)
                updated_entities_to_orders_table(None, name_data, address_data, tel_number_data, int(index_courier), 'preparing', customer_ordered)
               
            # update existing order status
            elif orders_menu_opt == 3:
                # show orders by index
                print('\nOrders list:\n')
                [print(f'index {el}\n{orders_list[el]}\n') for el in range(len(orders_list))]
                # print('Enter index of order to update')
                #        new_status = 
                index_order = int(input("Input index of order to update status: "))
                print('\nIndex -> Order Status')
                for index, o_status in enumerate(order_status):
                    print(f'index = {index} -> {o_status}')
                print('Enter index of current order status')
                index_order_status = int(input("Input index of order status: "))
                orders_list[index_order]['order_status'] = new_status = order_status[index_order_status]
                old_name = orders_list[index_order]['customer_name'] 
                updated_entities_to_orders_table(old_name, None, None, None, None, new_status, None)

            # update existing order 
            elif orders_menu_opt == 4:
                # show orders by index
                print('\nOrders list:\n')
                [print(f'index {el}\n{orders_list[el]}\n') for el in range(len(orders_list))]
                # get the index for an order to update
                index_order = tester_idx_input(len(orders_list))
                old_name = orders_list[index_order]['customer_name'] 
                new_name = orders_list[index_order]['customer_name'] 
                new_address = orders_list[index_order]['customer_address'] 
                new_phone = orders_list[index_order]['customer_phone'] 
                new_courier = orders_list[index_order]['courier'] 
                new_status = orders_list[index_order]['order_status'] 
                new_items = orders_list[index_order]['items'] 
                for index, item in enumerate(orders_list[index_order]): 
                    # update products by their index
                    if item == 'items':
                        order_prod_indexes = list(((filter(lambda x: products_list[int(x)]['name'], list(map(int, orders_list[index_order]['items'].split(',') ))))))
                        print("Order's current products:\nindex, product")
                        # show order's current products
                        [print(f'{el}     ', products_list[int(el)]['name']) for el in order_prod_indexes]
                        # show all products
                        print("\nFull products list:\nindex, product")
                        [print(f'{el}     ', products_list[int(el)]['name']) for el in range(len(products_list))]
                        # get all indexes for updated products
                        updated_property = input(f'\nEnter updated indexes separated by spaces (select from above options) ')
                        if  updated_property:
                            orders_list[index_order][item] = new_items = updated_property
                    else:
                        updated_property = input(f"Enter update for '{item}' or hit Enter to skip: ")
                        if updated_property:  
                            if item   == 'customer_name': 
                                new_name = updated_property
                            elif item == 'customer_address': 
                                new_address = updated_property
                            elif item == 'customer_phone': 
                                new_phone = updated_property
                            elif item == 'courier': 
                                new_courier = updated_property
                            elif item == 'order_status': 
                                new_status = updated_property
                            orders_list[index_order][item] = updated_property
                updated_entities_to_orders_table(old_name, new_name, new_address, int(new_phone), int(new_courier), new_status, new_items)

            # cancel order
            elif orders_menu_opt == 5:
                [print(f'index {el}\n{orders_list[el]}\n') for el in range(len(orders_list))]
                index_order = input("Enter index of order to delete or hit Enter to exit deletion: ")
                if index_order == '': 
                   break
                elif  type(index_order) != int: 
                    index_order = tester2_idx_input(len(orders_list))
                old_name = orders_list[index_order]['customer_name'] 
                #old_address = orders_list[index_order]['customer_name'] 
                if index_order == '': continue
                orders_list.pop(index_order) 
                print(orders_list)
                updated_entities_to_orders_table(old_name, None, None , None, None, None, None)
            
            # show orders list by order status
            elif orders_menu_opt == 6:
                orders_list_by_order_status = sorted(orders_list, key=lambda d: d['order_status']) 
                print('\nOrders list by order status:\n')
                [print(f'{orders_list_by_order_status[el]["order_status"]}:\n',orders_list_by_order_status[el]) for el in range(len(orders_list_by_order_status))]
            else:
                print("Invalid menu option. Please enter valid option.")  
                break
            print('\n* Orders menu *:')
            orders_menu_opt = int(input("Press 0 to go to main menu , 1 to see order data, 2 to add an order, \
            3 to update order status, 4 to update order,  5 to delete order, 6 to show orders list by order status: "))
    
    print('\n*** Main menu ***')
    hub_menu = int(input("Select 0 to exit program\nSelect 1 for products menu\nSelect 2 for couriers options \
    \nSelect 3 for orders options\nYour selection? "))


# save couriers list to txt file
save_couriers_txt(couriers)


# save products list to txt file
save_products_txt(cafe_products)


# save orders list of dicts to csv file
save_orders_csv(orders_list)


# save couriers list of dicts to csv file
save_couriers_csv(couriers_list)


# save products list of dicts to csv file
save_products_csv(products_list)
	

# exiting program
print("Goodbye")


# clear terminal
stdout.write('\x1b[H\x1b[2J') 
exit()


