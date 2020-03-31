from flask import Flask
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.item import item

app = server.app
api = server.api

items_db = [
    {'name': 'Chicken Platter', 'price': 9.99},
    {'name': 'Combo Platter', 'price': 14.99},
    {'name': 'Gyro Sandwich', 'price': 7.99}
]

# Get all the items in the store
@api.route('/items')
class ItemList(Resource):
    def get(self):
        return items_db
    
    # POST or create a new item
    @api.expect(item, validate=True)
    def post(self):
        new_item = {
            "name": api.payload["name"],
            "price": api.payload["price"]
        }
        items_db.append(new_item)
        return new_item
        

# GET/DELETE to /items/:name

@api.route('/item/<string:name>')
class Item(Resource):
    def get(self, name):
        for item in items_db:
            if item["name"] == name:
                return item
        return ("Sorry, Item not on Menu", 404)

    def delete(self, name):
        global items_db
        items_db = list(filter(lambda x: x["name"] != name, items_db))
        return items_db

    @api.expect(item, validate=True)
    def put(self, name):
        item = next(filter(lambda x: x["name"] == name, items_db), None)
        if item is None:
            item = {
                "name": api.payload["name"],
                "price": api.payload["price"]
            }
            items_db.append(item)
        else:
            item.update(api.payload)
        return item

        


