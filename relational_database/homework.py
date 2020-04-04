from typing import List
import psycopg2

def task_1_add_new_record_to_db(con) -> None:
    sql = """
    INSERT INTO customers (customerid, customername, contactname, address, city, postalcode, country)
    VALUES
    (%s, 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore') RETURNING customerid;
    """
    cursor = con.cursor()
    cursor.execute("SELECT customerid FROM customers ORDER BY customerid DESC LIMIT 1;")
    max_id = cursor.fetchall()
    cursor.execute(sql, (max_id))
    result = cursor.fetchall ()
    con.commit()
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
    result = cursor.fetchall ()
    con.commit()
    return result

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
    result = cursor.fetchall ()
    con.commit()
    return result


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    sql = """UPDATE customers SET customername = 'Johnny Depp' ORDER BY customerid = 1;"""
    sql1 = """SELECT * FROM customers """
    cursor = con.cursor
    cursor.execute(sql)
    cursor.execute(sql1)    
    result = cursor.fetchall ()
    con.commit()
    return result



def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    sql = """DELETE customers WHERE customerid = (SELECT MAX(customerid) FROM customers );"""
    sql1 = """SELECT * FROM customers """
    cursor = con.cursor
    cursor.execute(sql)    
    cursor.execute(sql1)  
    result = cursor.fetchall 
    con.commit()
    return result

nj;
def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    pass


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    pass


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    pass


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    pass


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    pass


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    pass


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    pass


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    pass


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    pass


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    pass


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    pass
