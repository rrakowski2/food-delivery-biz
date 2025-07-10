'''
utility module to load all data from files (txt, csv) to python or database tables and vice versa
'''

# Set compute environment
import csv
import pymysql
import os
from dotenv import load_dotenv


#### Function to pull mysql selected tables' records to csv data (products and couriers, orders?)


def load_record_to_CSVs():
    # Load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")

    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
                host = host_name,
                database = database_name,
                user = user_name,
                password = user_password
            ) as connection:
    
            print('Opening cursor...')
            # A cursor is an object that represents a DB cursor,
            # which is used to manage the context of a fetch operation.
            cursor = connection.cursor()
            # run SQL query to pull couriers table data to csv
            cursor.execute('SELECT name, phone, courier_id FROM couriers')      
            
            # get one result at a time with the below code
            column_names = ['name', 'phone']
            # give the CSV file a name
            filename = "couriers.csv"
            # setup and write data to the CSV File
            with open(filename, 'w') as csvfile:
    	         # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
    	         # write the column_names to the csv file
                writer.writeheader()
                lista = []
                print('Fetched records from couriers table:\n')
                while True:
                    # fetch one record into memory
                    row = cursor.fetchone()
                    if row == None:
                        break
                    courier_data = {}
                    courier_data['name'] = row[0]
                    courier_data['phone'] = row[1]
                    lista.append(courier_data)
                    # show the fetched record
                    print(f'courier_id = {row[2]}, name = {row[0]}, phone = {row[1]}')   
    	        #write the rows to the csv file
                writer.writerows(lista)

            # run SQL query to pull products table data to csv
            cursor.execute('SELECT name, price FROM products ORDER BY product_id ASC')
            # fetch all the rows into memory
            rows = cursor.fetchall()
            column_names = ['name', 'price']
            # give the CSV file a name
            filename = "products.csv"
            # setup and write data to the CSV File
            with open(filename, 'w') as csvfile:
    	        # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
    	         # write the column_names to the csv file
                writer.writeheader()
                listb = []
                for row in rows:
                    product_data = {}
                    product_data['name'] = row[0]
                    product_data['price'] = row[1]
                    listb.append(product_data)
    	        #write the rows to the csv file
                writer.writerows(listb)

            # close the cursor, with the context connection will automatically close 
            print('Closing cursor...')
            cursor.close()

    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')   


#### Function to pull all tables data from mysql database to csv file


def load_database_to_CSVs():
    # load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")

    try:
        print('Opening connection...')
        # establish a database connection
        with pymysql.connect(
                host = host_name,
                database = database_name,
                user = user_name,
                password = user_password
            ) as connection:
            cursor = connection.cursor()
            # run SQL query to pull orders table data to csv
            cursor.execute('SELECT customer_name, customer_address, customer_phone, courier, order_status, items, order_id FROM orders ORDER BY order_id ASC')
            # fetch all the rows into memory
            rows = cursor.fetchall()
            column_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'order_status', 'items']
            # give the CSV file a name
            filename = "orders.csv"
            # setup and write data to the CSV File
            with open(filename, 'w') as csvfile:
    	    # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
    	       # write the column_names to the csv file
                writer.writeheader()
                listc = []
                print('  ID   customer_name  customer_address      cust_phone courier order_status items')
                print(99 * "-",)
                for row in rows:
                    order_data = {}
                    order_data['customer_name'] = row[0]
                    order_data['customer_address'] = row[1]
                    order_data['customer_phone'] = row[2]
                    order_data['courier'] = row[3]
                    order_data['order_status'] = row[4]
                    order_data['items'] = row[5]
                    listc.append(order_data)
                    print("| {:<3d} | {:<10s} | {:<20s} | {:<11d} | {:<3d} | {:<10s} | {:<20s} |".format(row[6], row[0], row[1], row[2], row[3], row[4], row[5]))
                print(99 * "-",)
                #write the rows to the csv file
                writer.writerows(listc)

            # run SQL query to pull couriers table data to csv
            cursor.execute('SELECT name, phone, courier_id FROM couriers ORDER BY courier_id ASC')
            # fetch all the rows into memory
            rows = cursor.fetchall()
            column_names = ['name', 'phone']
            # give the CSV file a name
            filename = "couriers.csv"
            # setup and write data to the CSV File
            with open(filename, 'w') as csvfile:
    	    # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
    	       # write the column_names to the csv file
                writer.writeheader()
                lista = []
                print('  ID    Courier       Phone')
                print(33 * "-",)
                for row in rows:
                    courier_data = {}
                    courier_data['name'] = row[0]
                    courier_data['phone'] = row[1]
                    lista.append(courier_data)
                    print("| {:<3d} | {:<10s} | {:<11d} |".format(row[2], row[0], row[1]))
                print(33 * "-",)
                #write the rows to the csv file
                writer.writerows(lista)

            # run SQL query to pull products table data to csv
            cursor.execute('SELECT name, price, product_id FROM products ORDER BY product_id ASC')
            # fetch all the rows into memory
            rows = cursor.fetchall()
            column_names = ['name', 'price']
            # give the CSV file a name
            filename = "products.csv"
            # setup and write data to the CSV File
            with open(filename, 'w') as csvfile:
    	    # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
    	    # write the column_names to the csv file
                writer.writeheader()
                listb = []
                print('  ID    Product      Price')
                print(36 * "-",)
                for row in rows:
                    product_data = {}
                    product_data['name'] = row[0]
                    product_data['price'] = row[1]
                    listb.append(product_data)
                    print("| {:<3d} | {:<18s} | {:<6.2f} |".format(row[2], row[0], row[1]))
                print(36 * "-",)
    	        # write the rows to the csv file
                writer.writerows(listb)
            # commit changes
            connection.commit()
            # close the cursor, with the context connection will automatically close 
            #print('Closing cursor...')
            cursor.close()

    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')   


#### Function to push initial data (products and couriers) from csv files to mysql database (or in case of database corruption) 


def initial_CSVs_push_to_database():
    # load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")
    try:
        print('Opening connection...')
        # establish a database connection
        with pymysql.connect(
                host = host_name,
                database = database_name,
                user = user_name,
                password = user_password
            ) as connection:
            #print('Opening cursor...')
            # cursor is an object that represents  db cursor which is used to manage the context of a fetch operation.
            cursor = connection.cursor()
            cursor.execute("""TRUNCATE TABLE couriers""")
            cursor.execute("""TRUNCATE TABLE products""")
            cursor.execute("""TRUNCATE TABLE orders""")
            print('Inserting new record...')

            # insert a new record
             # load orders csv to database
            sql_o = """
                INSERT INTO orders (customer_name, customer_address, customer_phone, courier, order_status, items)  
                VALUES (%s, %s, %s, %s, %s, %s)
                """
            #csv_data = csv.reader(file('couriers.csv'))
            with open("orders.csv", 'r') as file:
                csv_data = csv.DictReader(file)
                for row in csv_data:
                    #print(tuple(row.values()))
                    cursor.execute(sql_o, tuple(row.values()))

            # load courier csv to database
            sql_c = """
                INSERT INTO couriers (name, phone) 
                VALUES (%s, %s)
                """
            #csv_data = csv.reader(file('couriers.csv'))
            with open("couriers.csv", 'r') as file:
                csv_data = csv.DictReader(file)
                for row in csv_data:
                    #print(tuple(row.values()))
                    cursor.execute(sql_c, tuple(row.values()))

            # load products csv to database
            sql_p = """
                INSERT INTO products (name, price) 
                VALUES (%s, %s)
                """
            with open("products.csv", 'r') as file:
                csv_data = csv.DictReader(file)
                for row in csv_data:
                    #print(tuple(row.values()))
                    cursor.execute(sql_p, tuple(row.values()))
            # commit the record
            connection.commit()

            # close the cursor, with the context connection will automatically close 
            print('Closing cursor...')
            cursor.close() # 

    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')


#### Function to push updated data (for products/couriers) to mysql database 


def updated_entities_push_to_database(old_data_1, new_data_1, old_data_2, new_data_2, case=None):
    # load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")

    try:
        #print('Opening connection...')
        # establish a database connection
        with pymysql.connect(
                host = host_name,
                database = database_name,
                user = user_name,
                password = user_password
            ) as connection:
    
            #print('Opening cursor...')
            # cursor is an object that represents  db cursor which is used to manage the context of a fetch operation.
            cursor = connection.cursor()

            # insert a new record
            data_values = ()            
            #print('\nInserting new record...')
               # couriers table
            if case:
                    # load courier's updated record to database
                    sql_add = """
                        INSERT INTO couriers (name, phone)
                        VALUES (%s, %s)
                        """
                    sql_del = """
                        DELETE FROM couriers WHERE name = %s
                        """
                    sql_update = """
                        UPDATE couriers SET name = %s, phone = %s
                        WHERE name = %s
                        """
                    # adding record to couriers table
                    if old_data_1 == None:
                        data_values = (str(new_data_1), int(new_data_2))
                        cursor.execute(sql_add, data_values)
                        print(f'| courier_id = {cursor.lastrowid} | name = {new_data_1} | phone = {new_data_2} | <- record added to table!')                    
                      
                    # removing record from table
                    elif new_data_1 == None:
                        data_values = (str(old_data_1))
                        cursor.execute(sql_del, data_values)
                        print(f'| courier_id = {cursor.lastrowid} | name = {old_data_1} | <- courier deleated!')   

                    # updating record in table
                    else:
                        data_values = (str(new_data_1), int(new_data_2), str(old_data_1))
                        cursor.execute(sql_update, data_values)  
                        print(f'| courier_id = {cursor.lastrowid} | name = {old_data_1} | got updated with: | name = {new_data_1} | phone = {new_data_2} | <- record updated in table!')          
                    # Commit the change
                    connection.commit()

                # products table   
            else:    
                    # load product's updated record to database
                    sql_add = """
                        INSERT INTO products (name, price)
                        VALUES (%s, %s)
                        """
                    sql_del = """
                        DELETE FROM products WHERE name = %s
                        """
                    sql_update = """
                        UPDATE products SET name = %s, price = %s
                        WHERE name = %s
                        """                               
                    # adding record to products table
                    if old_data_1 == None:
                        data_values = (str(new_data_1), float(new_data_2))
                        cursor.execute(sql_add, data_values)
                        print(f'| product_id = {cursor.lastrowid} | name = {new_data_1} | phone = {new_data_2} | <- record added to table!')                    

                    # removing record from table
                    elif new_data_1 == None:
                        data_values = (str(old_data_1))
                        cursor.execute(sql_del, data_values)
                        print(f'| product_id = {cursor.lastrowid} | name = {old_data_1} | <- product deleted!')

                    # updating record in table
                    else:
                        data_values = (str(new_data_1), float(new_data_2), str(old_data_1))
                        cursor.execute(sql_update, data_values) 
                        print(f'| product_id = {cursor.lastrowid} | name = {old_data_1} | got updated with: | name = {new_data_1} | phone = {new_data_2} | <- record updated in table!')            
                    # Commit the change
                    connection.commit()

            # close the cursor, with the context connection will automatically close 
            #print('Closing cursor...')
            cursor.close() # 

    except Exception as ex:
        print('Failed to:', ex)
    
    print('All done!')


#### Function to push updated data for orders to mysql database


def updated_entities_to_orders_table(old_name, new_name, new_address, new_phone, new_courier, new_status, new_items):
    # load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")

    try:
        #print('Opening connection...')
        # establish a database connection
        with pymysql.connect(
                host = host_name,
                database = database_name,
                user = user_name,
                password = user_password
            ) as connection:
    
            #print('Opening cursor...')
            # cursor is an object that represents  db cursor which is used to manage the context of a fetch operation.
            cursor = connection.cursor()

            # insert a new record
            data_values = ()            
            #print('\nInserting new record...')
            # orders table
            
            # load updated record for orders to database
            sql_add = """
                INSERT INTO orders (customer_name, customer_address, customer_phone, courier, order_status, items)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
            sql_del = """
                DELETE FROM orders WHERE customer_name = %s
                """
            sql_update = """
                UPDATE orders SET customer_name = %s, customer_address = %s, customer_phone = %s, courier = %s, order_status = %s, items = %s 
                WHERE customer_name = %s
                """   
            sql_status = """
                UPDATE orders SET order_status = %s
                WHERE customer_name = %s
                """                            
            # adding record to couriers table
            if old_name == None and new_items != None:
                data_values = (str(new_name), str(new_address), int(new_phone), int(new_courier), str(new_status), str(new_items))
                cursor.execute(sql_add, data_values)
                print(f'| order_id = {cursor.lastrowid} | customer_name = {new_name} | customer_address = {new_address} | customer_phone = {new_phone} | courier = {new_courier} | order_status = {new_status} | items = {new_items} | <- record added to orders!')                    
              
            # removing record from table
            elif new_name == None and new_status == None:
                data_values = (str(old_name))
                cursor.execute(sql_del, data_values)
                print(f'| order_id = {cursor.lastrowid} | customer_name = {old_name} | <- customer deleated!') 

            # updating order status in table
            elif bool(old_name) and bool(new_status) and new_items == None:
                print(old_name,new_status)
                data_values = (str(new_status), str(old_name))
                cursor.execute(sql_status, data_values)  
                print(f'| order_id = {cursor.lastrowid} | customer_name = {old_name} | order_status = {new_status} | <- record updated with new status in orders table!')    
            
            # updating record in table
            else:
                data_values = (str(new_name), str(new_address), int(new_phone), int(new_courier), str(new_status), str(new_items), str(old_name))
                cursor.execute(sql_update, data_values)  
                print(f'| order_id = {cursor.lastrowid} | customer_name = {old_name} | got updated with: | customer_name = {new_name} | customer_address = {new_address} | customer_phone = {new_phone} | courier = {new_courier} | order_status = {new_status} | items = {new_items} | <- record updated in orders table!')    
      
            # Commit the change
            connection.commit()
            # close the cursor, with the context connection will automatically close 
            #print('Closing cursor...')
            cursor.close() # 

    except Exception as ex:
        print('Failed to:', ex)

    print('All done!')


#### Functions to load TXTs/CSVs to miniproject.py variables
def load_products_txt():
    # load products data from file #cafe_products = ['cola', 'pepsi', '7up']
    with open('products.txt', 'r') as file:
        cafe_products = [line.strip() for line in file]
        return cafe_products


def load_couriers_txt():
    # load couriers data from file #couriers = ['Bob', 'Jon', 'Sally']
    with open('couriers.txt', 'r') as file:
        couriers = [line.strip() for line in file]
        return couriers


def load_products_csv():
    # load products list of dicts from csv file
    with open("products.csv", 'r') as file:
        products_dictionary = csv.DictReader(file)
        products_list = list(products_dictionary)
        print(products_list,'\n') 
        return products_list


def load_couriers_csv():
    # load couriers list of dicts from csv file
    with open("couriers.csv", 'r') as file:
       couriers_dictionary = csv.DictReader(file)
       couriers_list = list(couriers_dictionary)
       print(couriers_list,'\n') 
       return couriers_list


def load_orders_csv():
    # load couriers list of dicts from csv file
    with open("orders.csv", 'r') as file:
        orders_dictionary = csv.DictReader(file)
        orders_list = list(orders_dictionary)
        
        for dic in range(len(orders_list)):
           #dict[next(reversed(dict))]  # == dict values
           aux_list = list( map( int,orders_list[dic][next(reversed(orders_list[dic]))].split() ))
           string = ', '.join(map(str, aux_list))
           orders_list[dic][next(reversed(orders_list[dic]))] = string
        print(orders_list)
        return orders_list

    
#### Functions to load dict variables to CSVs 


# save all orders-list of dicts to csv file
def save_orders_csv(orders_list):
    for dic in range(len(orders_list)):
        orders_list[dic][next(reversed(orders_list[dic]))] = orders_list[dic][next(reversed(orders_list[dic]))].replace(',','')
    # define column names
    column_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'order_status', 'items']
    # give the CSV file a name
    filename = "orders.csv"
    # setup and write data to the CSV File
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = column_names)
        # write the column_names to the csv file 
        writer.writeheader()
    	# write the rows to the csv file
        writer.writerows(orders_list)
    	#print(writer)


# save products list of dicts to csv file
def save_products_csv(products_list):
    # define column names
    column_names = ['name', 'price']
    # give the CSV file a name
    filename = "products.csv"
    # setup and write data to the CSV File
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = column_names)
        # write the column_names to the csv file
        writer.writeheader()
    	# write the rows to the csv file
        writer.writerows(products_list)
    	#print(writer)


# save couriers list of dicts to csv file
def save_couriers_csv(couriers_list):
    # define column names
    column_names = ['name', 'phone']
    # give the CSV file a name
    filename = "couriers.csv"
    # setup and write data to the CSV File
    with open(filename, 'w') as csvfile:
    	# creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = column_names)
        # write the column_names to the csv file
        writer.writeheader()
    	# write the rows to the csv file
        writer.writerows(couriers_list)


#### Functions to load dict variables to .txt


# add couriers from a list to .txt
def save_couriers_txt(couriers):
    file = None
    try:
        open("couriers.txt", "w").close()
        file = open('couriers.txt', 'a')
        for item in couriers:
            file.write(item + '\n')
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    #else: 
        #file = open('couriers.txt', 'r')
        #var = file.read()
        #print(var)
    finally:
        if file:
            file.close()


#   add products from a list to .txt
def save_products_txt(cafe_products):
    file = None
    #print(cafe_products)
    try:
        open("products.txt", "w").close()
        file = open('products.txt', 'a')
        for item in cafe_products:
            file.write(item + '\n')
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    #else: 
        #file = open('products.txt', 'r')
        #var = file.read()
        #print(var)
    finally:
        if file:
            file.close()






























#cursor.execute('SELECT LAST_INSERT_ID()')
#all = cursor.fetchall()
#print(all)

'''
cursor.execute('SHOW KEYS FROM products WHERE Key_name = "PRIMARY"')
all = cursor.fetchall()
print(all)
connection.commit()
'''

#cursor.execute('SHOW KEYS FROM <table_name> WHERE Key_name = "PRIMARY"')
#all = cursor.fetchall()
#print(all)

#print(f"| {row[2]:3d} | {row[0]:<10s} | {row[1]:10d} |")
#print(f'courier_id={row[2]}, name={row[0]}, phone={row[1]}') 

#cursor.execute('SHOW INDEX FROM couriers WHERE Key_name = "PRIMARY"') # cursor.fetchone()[3]   connection.insert_id() = cursor.lastrowid()
#print(f'courier_id={cursor.fetchone()[3]}, name={row[0]}, phone={row[1]}')    

#final = input(f'Are you sure to del the order indexed {index_order}? input y for yes or n for no')
  #  if final == 'y': break