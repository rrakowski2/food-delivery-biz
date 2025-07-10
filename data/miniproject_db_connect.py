# File to load csv data (products and couriers) to mysql database

import csv
import pymysql
import os
from dotenv import load_dotenv

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

######### Pull data from  csv files to mysql database ###########

        print('Inserting new record...')
        # Insert a new record
        
        # load courier csv to database
        sql_c = """
            INSERT INTO couriers (name, phone) 
            VALUES (%s, %s)
            """
        #csv_data = csv.reader(file('couriers.csv'))
        with open("couriers.csv", 'r') as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:
                print(tuple(row.values()))
                cursor.execute(sql_c, tuple(row.values()))

        # load products csv to database
        sql_p = """
            INSERT INTO products (name, price) 
            VALUES (%s, %s)
            """
        with open("products.csv", 'r') as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:
                print(tuple(row.values()))
                cursor.execute(sql_p, tuple(row.values()))
        # Commit the record
        connection.commit()

        ######### Pull data from mysql database to csv files ###########

        # Execute SQL query
        cursor.execute('SELECT name, phone FROM couriers ORDER BY courier_id ASC')
        # Fetch all the rows into memory
        rows = cursor.fetchall()

        print('Displaying all records...')
        # Gets all rows from the result
        for row in rows:
            print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')

        # Can alternatively get one result at a time with the below code
        # while True:
        #     row = cursor.fetchone()
        #     if row == None:
        #         break
        #     print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')

        print('Closing cursor...')
        # Closes the cursor so will be unusable from this point 
        cursor.close()
        
        # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')