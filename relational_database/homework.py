from typing import List
import psycopg2

def task_1_add_new_record_to_db(con) -> None:
    sql = """
    INSERT INTO customers (customerid, customername, contactname, address, city, postalcode, country)
    VALUES
    (%s, 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore') RETURNING customerid;
    """
    cursor = con.cursor()
    cursor.execute("INSERT INTO Customers (Customername, Contactname, Address, City, Postalcode, Country) "
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore',))
    con.commit()
    result = cursor.fetchall ()
    return result
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    sql = """SELECT * FROM customers """
    cursor = cur.cursor
    cursor.execute(sql)    
    return  cursor.fetchall ()

def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = """SELECT * FROM customers WHERE country == 'Germany'"""
    cursor = cur.cursor
    cursor.execute(sql)    

    return cursor.fetchall ()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    sql = """UPDATE customers SET customername = 'Johnny Depp' ORDER BY customerid = 1;"""
    cursor = con.cursor
    cursor.execute(sql)
    con.commit()



def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    sql = """DELETE customers WHERE customerid = (SELECT MAX(customerid) FROM customers );"""
    cursor = con.cursor
    cursor.execute(sql)    
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    sql = """SELECT country from suppliers;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall() 
    


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    sql = """SELECT city from suppliers ORDER BY city DESC;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
    


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    sql = """SELECT count (customername), city from customers GROUP BY city;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall ()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = """SELECT count (customername), city from customers WHERE count (customername) > 10  GROUP BY city HAVING count (customername) > 10;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
    


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    sql = """SELECT * from customers ORDER BY customeridcustomerid  LIMIT 10;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = """SELECT * from customers ORDER BY customeridcustomerid  WHERE customeridcustomerid > 11;"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    sql = """SELECT * from suppliers ORDER BY customeridcustomerid  WHERE city = 'USA' OR city = 'UK' OR city = 'Japan';"""
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
    


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = """SELECT suppliers .city, products.ProductName,  products.SupplierID,  products.CategoryID
            FROM suppliers
            LEFT JOIN  products
            WHERE suppliers .city = 'Sweden';""" 
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
    


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    sql = """SELECT *
            FROM products
            JOIN  suppliers
            ON products.SupplierID =  suppliers.SupplierID;""" 
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
    


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    sql = """SELECT *
            FROM products
            JOIN  suppliers
            ON products.CustomerID =  suppliers.CustomerID;""" 
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    sql = """SELECT *
            FROM products
            JOIN  suppliers
            ON products.country =  suppliers.country
            ORDER BY country;""" 
    cursor = cur.cursor
    cursor.execute(sql)    
    return cursor.fetchall()
