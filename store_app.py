from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'
    
class NoSuchStoreID(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


app = Flask(__name__)

@app.errorhandler(NoSuchUserError)
@app.errorhandler(NoSuchStoreID)
def my_error_handler(e):
	return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>',methods = ['GET'])
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    update_user = db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status':'success'})

@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    goods_count = db.goods.add_goods(request.json)
    return jsonify({'number of created goods': goods_count }), 201

@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    get_good = db.goods.get_goods_by_id()
    return jsonify(get_good)

@app.route('/goods', methods = ['PUT'])
def update_goods():
    db = inject.instance('DB')
    successful_update, update_with_error = db.goods.update_goods(request.json)
    return jsonify(
        {
            'successfully_updated': successful_update, 
            'errors': {'No such id in goods': update_with_error}
            })

@app.route('/store', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    store_id = db.stores.add(request.json)
    return jsonify({'user_id': store_id}), 201


@app.route('/store/<int:store_id>',methods = ['GET'])
def get_store(store_id):
    db = inject.instance('DB')
    store = db.users.get_user_by_id(store_id)
    return jsonify(store)


@app.route('/store/<int:store_id>', methods = ['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    db.users.get_user_by_id(request.json['manager_id'])
    update_store = db.users.update_store_by_id(store_id, request.json)
    return jsonify({'status':'success'})