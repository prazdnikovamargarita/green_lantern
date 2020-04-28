from flask import Flask, jsonify, request
from fake_storage import FakeStorage
from store_app import app 
import inject

def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name':'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name':'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name':'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name':'John Doe'}

    def test_get_unexistent_user(self):
        
        resp = self.client.post(
            '/users',
            json={'name':'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get('/users/3')
        assert resp.status_code == 404
        assert resp.json == {'error':'No such user_id 3 '}
    def test_successful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name':'John Doe'}
        )
        u = resp.json['user_id']
        resp = self.client.put(
            '/users/%{user_id}'%(user_id),
            json={'name':'Johanna Doe'}
        )
        assert resp.status_code == 201
        assert resp.json== {'status':'success'}
    
    def test_update_unexistent_user(self):
        resp = self.client.post(
            '/users',
            json={'name':'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            '/users/3',
            json={'name':'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error':'No such user_id 3'}

class TestGoods(Initializer):
    def test_create_new(self):
        resp = self.client.post(
        '/goods',
            json=[{'name': 'Chocolate_bar', 'price': 10},
                  {'name': 'Snickers', 'price': 19},
                  {'name': 'Mars', 'price': 9.5},
                  {'name': 'Kinder_Chocolate', 'price': 26},
                  {'name': 'Nesquik', 'price': 25},
                  {'name': 'Bounty', 'price': 11.2},
                  {'name': 'Twix', 'price': 9.3},
                  {'name': 'Milky_Way', 'price': 10},
                  {'name': 'Milka&Daim', 'price': 20},
                  {'name': 'M&Ms', 'price': 21}]
        )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 10}
        resp = self.client.post(
            '/goods',
            json=[{'name': 'Olenka', 'price': 15}]
        )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 1}


    def test_get_goods(self):
        resp = self.client.post(
            '/goods',
            json=({'name': 'Chocolate_bar', 'price': 10},
                  {'name': 'Snickers', 'price': 19},
                  {'name': 'Mars', 'price': 9.5},
                  {'name': 'Kinder_Chocolate', 'price': 26},
                  {'name': 'Nesquik', 'price': 25},
                  {'name': 'Bounty', 'price': 11.2},
                  {'name': 'Twix', 'price': 9.3},
                  {'name': 'Milky_Way', 'price': 10},
                  {'name': 'Milka&Daim', 'price': 20},
                  {'name': 'M&Ms', 'price': 21})
        )
        resp = self.client.get(f'/{%goods}')
        assert resp.status_code == 200
        assert resp.json == [{'name': 'Chocolate_bar', 'price': 10, 'id': 1},
                             {'name': 'Snickers', 'price': 19, 'id': 2},
                             {'name': 'Mars', 'price': 9.5, 'id': 3},
                             {'name': 'Kinder_Chocolate', 'price': 26, 'id': 4},
                             {'name': 'Nesquik', 'price': 25, 'id': 5},
                             {'name': 'Bounty', 'price': 11.2, 'id': 6},
                             {'name': 'Twix', 'price': 9.3, 'id': 7},
                             {'name': 'Milky_Way', 'price': 10, 'id': 8},
                             {'name': 'Milka&Daim', 'price': 20, 'id': 9},
                             {'name': 'M&Ms', 'price': 21, 'id': 10}]
    def test_update_goods(self):
        resp = self.client.post(
            '/goods',
            json=(
                {'name': 'Chocolate_bar', 'price': 10, 'id': 1},
                {'name': 'Snickers', 'price': 19, 'id': 2},
                {'name': 'Mars', 'price': 9.5, 'id': 3},
                {'name': 'Kinder_Chocolate', 'price': 26, 'id': 4},
                {'name': 'Nesquik', 'price': 25, 'id': 5},
                {'name': 'Bounty', 'price': 11.2, 'id': 6},
                {'name': 'Twix', 'price': 9.3, 'id': 7},
                {'name': 'Milky_Way', 'price': 10, 'id': 8},
                {'name': 'Milka&Daim', 'price': 20, 'id': 9},
                {'name': 'M&Ms', 'price': 21, 'id': 10})
        )
        resp = self.client.put('/{goods}',
                               json=({'name': 'Chocolate_bar', 'price': 1, 'id': 1},
                                     {'fname': 'Snickers', 'price': 19, 'id': 2},
                                     {'name': 'Mars', 'price': 9.5, 'id': 3},
                                     {'name': 'Kinder_Chocolate', 'price': 26, 'id': 4},
                                     {'name': 'Nesquik', 'price': 25, 'id': 5},
                                     {'name': 'Milk', 'price': 25, 'id': 12},
                                     {'name': 'Choko', 'price': 25, 'id': 13},
                                     {'name': 'Coffe', 'price': 25, 'id': 14})
                               )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 5, 'errors': {'No such id in goods': [12, 13, 14]}}


class TestShops(Initializer):
    def test_create_store(self): 
        resp = self.client.post('/users',
                                json={"name": "Mark Miller"})
        resp = self.client.post('/users',
                                json={"name": "Walter White"})
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

   
    def test_successful_get_store(self):

        resp = self.client.post('/users',
                                json={"name": "Mark Miller"})
        resp = self.client.post('/users',
                                json={"name": "Walter White"})

        user_id = resp.json['user_id']
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': f'%{user_id}'}
        )
        store_id = resp.json['store_id']
        resp = self.client.get(f'/store/{store_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}


    def test_get_unexistent_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}
        )
        resp = self.client.get('/store/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 3'}

    def test_successful_update_store(self):
        resp = self.client.post('/users',
                                json={"name": "Mark Miller"})
        resp = self.client.post('/users',
                                json={"name": "Walter White"})
        user_id = resp.json['user_id']
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': f'%{user_id}'}
        )
        store_id = resp.json['store_id']
        resp = self.client.put(
            f'/store/f{store_id}',
            json={'name': 'Lazy Cat', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_store(self):
        
        resp = self.client.post('/users',
                                json={"name": "Mark Miller"})

        resp = self.client.put(
            '/store/3',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 4}
        )
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 4}
        )

        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 3'}
	assert resp.json == {'error': 'No such user_id 4'}
