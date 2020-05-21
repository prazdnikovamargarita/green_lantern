import csv


def get_users():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users

def get_stores():
    with open('stores.csv', 'r') as d:
        reader = csv.DictReader(d)
        stores = [i for i in reader]
    return stores

def get_goods():
    with open('goods.csv', 'r') as k:
        reader = csv.DictReader(k)
        goods = [i for i in reader]
    return goods

