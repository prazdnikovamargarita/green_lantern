from itertools import count
from store_app import NoSuchUserError, NoSuchStoreID

class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users
    @property 
    def goods (self):
        return self._goods
    @property
    def stores (self):
        return self._stores

class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    
    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add_goods(self, goods):
        for good in goods:
            good['id'] = next(self._id_counter)
            goods [good['id']] = good
        return len(goods)

    def get_goods_by_id(self, good):
        return [self._goods[good] for good in range(1, len(self._goods) + 1)]

    def successful_update (self, goods, good):
        updated_goods = 0
        errors_update = []
        for good in goods:
            goods_id = good['id']
            if goods_id in self._goods:
                self._goods[goods_id] = good
                updated_goods += 1
            else:
                errors_update.append(goods_id)
        return updated_goods, errors_update
            

class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, store):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreID(store_id)

    
    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreID(store_id)

